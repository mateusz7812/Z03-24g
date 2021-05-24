"""
    Messages server

    SAFRSAPI  # noqa: E501

    The version of the OpenAPI document: 0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.conversations_api import ConversationsApi  # noqa: E501


class TestConversationsApi(unittest.TestCase):
    """ConversationsApi unit test stubs"""

    def setUp(self):
        self.api = ConversationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_conversation0(self):
        """Test case for create_conversation0

        Create Conversation  # noqa: E501
        """
        pass

    def test_delete_conversationfrom_conversations0(self):
        """Test case for delete_conversationfrom_conversations0

        Delete Conversation from Conversations  # noqa: E501
        """
        pass

    def test_retrieve_conversationinstance0(self):
        """Test case for retrieve_conversationinstance0

        Retrieve Conversation instance  # noqa: E501
        """
        pass

    def test_retrieve_membershipfrommemberships1(self):
        """Test case for retrieve_membershipfrommemberships1

        Retrieve Membership from memberships  # noqa: E501
        """
        pass

    def test_retrieve_messagefrommessages0(self):
        """Test case for get_messages

        Retrieve Message from messages  # noqa: E501
        """
        pass

    def test_retrieve_userfromusers0(self):
        """Test case for retrieve_userfromusers0

        Retrieve User from users  # noqa: E501
        """
        pass

    def test_retrieveacollectionof_conversationobjects0(self):
        """Test case for retrieveacollectionof_conversationobjects0

        Retrieve a collection of Conversation objects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()