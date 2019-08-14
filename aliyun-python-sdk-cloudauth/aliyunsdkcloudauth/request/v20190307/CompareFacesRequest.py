# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkcloudauth.endpoint import endpoint_data

class CompareFacesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'CompareFaces','cloudauth')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SourceImageType(self):
		return self.get_body_params().get('SourceImageType')

	def set_SourceImageType(self,SourceImageType):
		self.add_body_params('SourceImageType', SourceImageType)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_TargetImageType(self):
		return self.get_body_params().get('TargetImageType')

	def set_TargetImageType(self,TargetImageType):
		self.add_body_params('TargetImageType', TargetImageType)

	def get_SourceImageValue(self):
		return self.get_body_params().get('SourceImageValue')

	def set_SourceImageValue(self,SourceImageValue):
		self.add_body_params('SourceImageValue', SourceImageValue)

	def get_TargetImageValue(self):
		return self.get_body_params().get('TargetImageValue')

	def set_TargetImageValue(self,TargetImageValue):
		self.add_body_params('TargetImageValue', TargetImageValue)