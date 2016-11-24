class NetworkService:
    def __init__(self, client):
        self.client = client



    def GET_network(self, headers=None, query_params=None):
        """
        Get a list of networks this user owns or can view/edit
        It is method for GET /network
        """
        uri = self.client.base_url + "/network"
        return self.client.session.get(uri, headers=headers, params=query_params)


    def POST_network(self, data, headers=None, query_params=None):
        """
        Create a new network
        It is method for POST /network
        """
        uri = self.client.base_url + "/network"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def GET_network_id(self, id, headers=None, query_params=None):
        """
        Get network configuration and status information
        It is method for GET /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.session.get(uri, headers=headers, params=query_params)


    def POST_network_id(self, data, id, headers=None, query_params=None):
        """
        Update network configuration
        It is method for POST /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.post(uri, data, headers=headers, params=query_params)


    def DELETE_network_id(self, id, headers=None, query_params=None):
        """
        Delete network
        It is method for DELETE /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def GET_network_id_member(self, id, headers=None, query_params=None):
        """
        Get a list of network members
        It is method for GET /network/{id}/member
        """
        uri = self.client.base_url + "/network/"+id+"/member"
        return self.client.session.get(uri, headers=headers, params=query_params)


    def GET_network_id_member_address(self, address, id, headers=None, query_params=None):
        """
        Get network member settings
        It is method for GET /network/{id}/member/{address}
        """
        uri = self.client.base_url + "/network/"+id+"/member/"+address
        return self.client.session.get(uri, headers=headers, params=query_params)


    def POST_network_id_member_address(self, data, address, id, headers=None, query_params=None):
        """
        Update member settings
        It is method for POST /network/{id}/member/{address}
        """
        uri = self.client.base_url + "/network/"+id+"/member/"+address
        return self.client.post(uri, data, headers=headers, params=query_params)
