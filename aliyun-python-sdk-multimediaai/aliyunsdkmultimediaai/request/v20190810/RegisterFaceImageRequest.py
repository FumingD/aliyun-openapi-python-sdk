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
from aliyunsdkmultimediaai.endpoint import endpoint_data

class RegisterFaceImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'multimediaai', '2019-08-10', 'RegisterFaceImage','multimediaai')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FaceGroupId(self):
		return self.get_query_params().get('FaceGroupId')

	def set_FaceGroupId(self,FaceGroupId):
		self.add_query_param('FaceGroupId',FaceGroupId)

	def get_FacePersonId(self):
		return self.get_query_params().get('FacePersonId')

	def set_FacePersonId(self,FacePersonId):
		self.add_query_param('FacePersonId',FacePersonId)

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)