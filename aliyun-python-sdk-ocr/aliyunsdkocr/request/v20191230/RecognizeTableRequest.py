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
from aliyunsdkocr.endpoint import endpoint_data

class RecognizeTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ocr', '2019-12-30', 'RecognizeTable','ocr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ImageType(self):
		return self.get_body_params().get('ImageType')

	def set_ImageType(self,ImageType):
		self.add_body_params('ImageType', ImageType)

	def get_UseFinanceModel(self):
		return self.get_body_params().get('UseFinanceModel')

	def set_UseFinanceModel(self,UseFinanceModel):
		self.add_body_params('UseFinanceModel', UseFinanceModel)

	def get_SkipDetection(self):
		return self.get_body_params().get('SkipDetection')

	def set_SkipDetection(self,SkipDetection):
		self.add_body_params('SkipDetection', SkipDetection)

	def get_ImageURL(self):
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self,ImageURL):
		self.add_body_params('ImageURL', ImageURL)

	def get_OutputFormat(self):
		return self.get_body_params().get('OutputFormat')

	def set_OutputFormat(self,OutputFormat):
		self.add_body_params('OutputFormat', OutputFormat)

	def get_AssureDirection(self):
		return self.get_body_params().get('AssureDirection')

	def set_AssureDirection(self,AssureDirection):
		self.add_body_params('AssureDirection', AssureDirection)

	def get_HasLine(self):
		return self.get_body_params().get('HasLine')

	def set_HasLine(self,HasLine):
		self.add_body_params('HasLine', HasLine)