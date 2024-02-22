from unittest.mock import patch

from django.test import TestCase

from core.utils import send_sqs_message, sqs


class TestSendSQSMessage(TestCase):
    def setUp(self):
        self.test_message = 'test message'
        self.test_queue_name = 'test_queue'
        self.test_queue_url = 'https://my-queue-url'
        self.test_return_value = {'MessageId': 'XXXXXXXX'}

    @patch('core.utils.sqs.get_queue_url')
    @patch('core.utils.sqs.create_queue')
    @patch('core.utils.sqs.send_message')
    def test_send_sqs_message_existing_queue(
        self,
        mock_send_message,
        mock_create_queue,
        mock_get_queue_url,
    ):
        # Mock SQS responses
        mock_get_queue_url.return_value = {'QueueUrl': self.test_queue_url}
        mock_send_message.return_value = self.test_return_value
        # Call the function
        result = send_sqs_message(self.test_queue_name, self.test_message)
        # Assertions
        mock_send_message.assert_called_once_with(
            QueueUrl=self.test_queue_url,
            MessageBody=self.test_message,
        )
        mock_create_queue.assert_not_called()
        self.assertEqual(result, self.test_return_value)

    @patch('core.utils.sqs.get_queue_url')
    @patch('core.utils.sqs.create_queue')
    @patch('core.utils.sqs.send_message')
    def test_send_sqs_message_creating_new_queue(
        self,
        mock_send_message,
        mock_create_queue,
        mock_get_queue_url,
    ):
        # Mock the get_queue_url method to raise QueueDoesNotExist
        mock_get_queue_url.side_effect = sqs.exceptions.QueueDoesNotExist(
            error_response={'Error': {'Code': 404}},
            operation_name='test',
        )
        # Mock SQS responses
        mock_create_queue.return_value = {'QueueUrl': self.test_queue_url}
        mock_send_message.return_value = self.test_return_value
        # Call the function
        result = send_sqs_message(self.test_queue_name, self.test_message)
        # Assertions
        mock_create_queue.assert_called_once_with(
            QueueName=f'bhub-{self.test_queue_name}',
        )
        self.assertEqual(result, self.test_return_value)
