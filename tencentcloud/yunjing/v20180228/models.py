# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class Account(AbstractModel):
    """帐号列表信息数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param Username: 帐号名。
        :type Username: str
        :param Groups: 帐号所属组。
        :type Groups: str
        :param Privilege: 帐号类型。
<li>ORDINARY：普通帐号</li>
<li>SUPPER：超级管理员帐号</li>
        :type Privilege: str
        :param AccountCreateTime: 帐号创建时间。
        :type AccountCreateTime: str
        :param LastLoginTime: 帐号最后登录时间。
        :type LastLoginTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.Groups = None
        self.Privilege = None
        self.AccountCreateTime = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.Groups = params.get("Groups")
        self.Privilege = params.get("Privilege")
        self.AccountCreateTime = params.get("AccountCreateTime")
        self.LastLoginTime = params.get("LastLoginTime")


class AccountStatistics(AbstractModel):
    """帐号统计数据。

    """

    def __init__(self):
        """
        :param Username: 用户名。
        :type Username: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.Username = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.MachineNum = params.get("MachineNum")


class AgentVul(AbstractModel):
    """主机漏洞信息

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param VulName: 漏洞名称。
        :type VulName: str
        :param VulLevel: 漏洞危害等级。
<li>HIGH：高危</li>
<li>MIDDLE：中危</li>
<li>LOW：低危</li>
<li>NOTICE：提示</li>
        :type VulLevel: str
        :param LastScanTime: 最后扫描时间。
        :type LastScanTime: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulId: 漏洞种类ID。
        :type VulId: int
        :param VulStatus: 漏洞状态。
<li>UN_OPERATED : 待处理</li>
<li>FIXED : 已修复</li>
        :type VulStatus: str
        """
        self.Id = None
        self.MachineIp = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.Description = None
        self.VulId = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")
        self.VulStatus = params.get("VulStatus")


class BruteAttack(AbstractModel):
    """暴力破解列表

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Status: 破解事件状态
<li>BRUTEATTACK_FAIL_ACCOUNT： 暴力破解事件-失败(存在帐号)  </li>
<li>BRUTEATTACK_FAIL_NOACCOUNT：暴力破解事件-失败(帐号不存在)</li>
<li>BRUTEATTACK_SUCCESS：暴力破解事件-成功</li>
        :type Status: str
        :param UserName: 用户名称。
        :type UserName: str
        :param City: 城市ID。
        :type City: int
        :param Country: 国家ID。
        :type Country: int
        :param Province: 省份ID。
        :type Province: int
        :param SrcIp: 来源IP。
        :type SrcIp: str
        :param Count: 尝试破解次数。
        :type Count: int
        :param CreateTime: 发生时间。
        :type CreateTime: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.Count = None
        self.CreateTime = None
        self.MachineName = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.Uuid = params.get("Uuid")


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion请求参数结构体

    """

    def __init__(self):
        """
        :param Quuid: 主机唯一标识Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self.Quuid = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Component(AbstractModel):
    """组件列表数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param ComponentVersion: 组件版本号。
        :type ComponentVersion: str
        :param ComponentType: 组件类型。
<li>SYSTEM：系统组件</li>
<li>WEB：WEB组件</li>
        :type ComponentType: str
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ModifyTime: 组件检测更新时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.ComponentVersion = None
        self.ComponentType = None
        self.ComponentName = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ComponentVersion = params.get("ComponentVersion")
        self.ComponentType = params.get("ComponentType")
        self.ComponentName = params.get("ComponentName")
        self.ModifyTime = params.get("ModifyTime")


class ComponentStatistics(AbstractModel):
    """组件统计数据。

    """

    def __init__(self):
        """
        :param Id: 组件ID。
        :type Id: int
        :param MachineNum: 主机数量。
        :type MachineNum: int
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ComponentType: 组件类型。
<li>WEB：web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param Description: 组件描述。
        :type Description: str
        """
        self.Id = None
        self.MachineNum = None
        self.ComponentName = None
        self.ComponentType = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineNum = params.get("MachineNum")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Description = params.get("Description")


class CreateProcessTaskRequest(AbstractModel):
    """CreateProcessTask请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class CreateProcessTaskResponse(AbstractModel):
    """CreateProcessTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUsualLoginPlacesRequest(AbstractModel):
    """CreateUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuids: 云镜客户端UUID数组。
        :type Uuids: list of str
        :param Places: 登录地域信息数组。
        :type Places: list of Place
        """
        self.Uuids = None
        self.Places = None


    def _deserialize(self, params):
        self.Uuids = params.get("Uuids")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)


class CreateUsualLoginPlacesResponse(AbstractModel):
    """CreateUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 暴力破解事件Id数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马记录ID数组
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 异地登录事件Id数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsualLoginPlacesRequest(AbstractModel):
    """DeleteUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端Uuid
        :type Uuid: str
        :param CityIds: 已添加常用登录地城市ID数组
        :type CityIds: list of int non-negative
        """
        self.Uuid = None
        self.CityIds = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.CityIds = params.get("CityIds")


class DeleteUsualLoginPlacesResponse(AbstractModel):
    """DeleteUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号用户名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号统计列表记录总数。
        :type TotalCount: int
        :param AccountStatistics: 帐号统计列表。
        :type AccountStatistics: list of AccountStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self.AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self.AccountStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Uuid表示，查询该主机下列表信息。
        :type Uuid: str
        :param Username: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Username表示，查询该用户名下列表信息。
        :type Username: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
<li>Privilege - String - 是否必填：否 - 帐号类型（ORDINARY: 普通帐号 | SUPPER: 超级管理员帐号）</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Username = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Username = params.get("Username")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号列表记录总数。
        :type TotalCount: int
        :param Accounts: 帐号数据列表。
        :type Accounts: list of Account
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Accounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentVulsRequest(AbstractModel):
    """DescribeAgentVuls请求参数结构体

    """

    def __init__(self):
        """
        :param VulType: 漏洞类型。
<li>WEB: Web应用漏洞</li>
<li>SYSTEM：系统组件漏洞</li>
<li>BASELINE：安全基线</li>
        :type VulType: str
        :param Uuid: 客户端UUID。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）
        :type Filters: list of Filter
        """
        self.VulType = None
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAgentVulsResponse(AbstractModel):
    """DescribeAgentVuls返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param AgentVuls: 主机漏洞信息
        :type AgentVuls: list of AgentVul
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AgentVuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AgentVuls") is not None:
            self.AgentVuls = []
            for item in params.get("AgentVuls"):
                obj = AgentVul()
                obj._deserialize(item)
                self.AgentVuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmAttributeRequest(AbstractModel):
    """DescribeAlarmAttribute请求参数结构体

    """


class DescribeAlarmAttributeResponse(AbstractModel):
    """DescribeAlarmAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param Offline: 防护软件离线告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type Offline: str
        :param Malware: 发现木马告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type Malware: str
        :param NonlocalLogin: 发现异地登录告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type NonlocalLogin: str
        :param CrackSuccess: 被暴力破解成功告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type CrackSuccess: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Offline = None
        self.Malware = None
        self.NonlocalLogin = None
        self.CrackSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offline = params.get("Offline")
        self.Malware = params.get("Malware")
        self.NonlocalLogin = params.get("NonlocalLogin")
        self.CrackSuccess = params.get("CrackSuccess")
        self.RequestId = params.get("RequestId")


class DescribeBruteAttacksRequest(AbstractModel):
    """DescribeBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 -  查询关键字</li>
<li>Status - String - 是否必填：否 -  查询状态（FAILED：破解失败 |SUCCESS：破解成功）</li>
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        """
        self.Uuid = None
        self.Offset = None
        self.Filters = None
        self.Limit = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")


class DescribeBruteAttacksResponse(AbstractModel):
    """DescribeBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 事件数量
        :type TotalCount: int
        :param BruteAttacks: 暴力破解事件列表
        :type BruteAttacks: list of BruteAttack
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BruteAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = BruteAttack()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentInfoRequest(AbstractModel):
    """DescribeComponentInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ComponentId: 组件ID。
        :type ComponentId: int
        """
        self.ComponentId = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")


class DescribeComponentInfoResponse(AbstractModel):
    """DescribeComponentInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 组件ID。
        :type Id: int
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ComponentType: 组件类型。
<li>WEB：web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param Homepage: 组件官网。
        :type Homepage: str
        :param Description: 组件描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.ComponentName = None
        self.ComponentType = None
        self.Homepage = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Homepage = params.get("Homepage")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
ComponentName - String - 是否必填：否 - 组件名称
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 组件统计列表记录总数。
        :type TotalCount: int
        :param ComponentStatistics: 组件统计列表数据数组。
        :type ComponentStatistics: list of ComponentStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComponentStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self.ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self.ComponentStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentsRequest(AbstractModel):
    """DescribeComponents请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Uuid和ComponentId必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param ComponentId: 组件ID。Uuid和ComponentId必填其一，使用ComponentId表示，查询该组件列表信息。
        :type ComponentId: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ComponentVersion - String - 是否必填：否 - 组件版本号</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.ComponentId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ComponentId = params.get("ComponentId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeComponentsResponse(AbstractModel):
    """DescribeComponents返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 组件列表记录总数。
        :type TotalCount: int
        :param Components: 组件列表数据。
        :type Components: list of Component
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Components = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号变更历史列表记录总数。
        :type TotalCount: int
        :param HistoryAccounts: 帐号变更历史数据数组。
        :type HistoryAccounts: list of HistoryAccount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HistoryAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self.HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self.HistoryAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImpactedHostsRequest(AbstractModel):
    """DescribeImpactedHosts请求参数结构体

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID。
        :type VulId: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED：待处理 | FIXED：已修复）</li>
        :type Filters: list of Filter
        """
        self.VulId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeImpactedHostsResponse(AbstractModel):
    """DescribeImpactedHosts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param ImpactedHosts: 漏洞影响机器列表数组
        :type ImpactedHosts: list of ImpactedHost
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImpactedHosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImpactedHosts") is not None:
            self.ImpactedHosts = []
            for item in params.get("ImpactedHosts"):
                obj = ImpactedHost()
                obj._deserialize(item)
                self.ImpactedHosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo返回参数结构体

    """

    def __init__(self):
        """
        :param MachineIp: 机器ip。
        :type MachineIp: str
        :param ProtectDays: 受云镜保护天数。
        :type ProtectDays: int
        :param MachineOs: 操作系统。
        :type MachineOs: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineStatus: 在线状态。
<li>ONLINE： 在线</li>
<li>OFFLINE：离线</li>
        :type MachineStatus: str
        :param InstanceId: CVM或BM主机唯一标识。
        :type InstanceId: str
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param Quuid: CVM或BM主机唯一Uuid。
        :type Quuid: str
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param IsProVersion: 是否开通专业版。
<li>true：是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param ProVersionOpenDate: 专业版开通时间。
        :type ProVersionOpenDate: str
        :param MachineType: 云主机类型。
<li>CVM: 虚拟主机</li>
<li>BM: 黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineIp = None
        self.ProtectDays = None
        self.MachineOs = None
        self.MachineName = None
        self.MachineStatus = None
        self.InstanceId = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.IsProVersion = None
        self.ProVersionOpenDate = None
        self.MachineType = None
        self.MachineRegion = None
        self.PayMode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.ProtectDays = params.get("ProtectDays")
        self.MachineOs = params.get("MachineOs")
        self.MachineName = params.get("MachineName")
        self.MachineStatus = params.get("MachineStatus")
        self.InstanceId = params.get("InstanceId")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.ProVersionOpenDate = params.get("ProVersionOpenDate")
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.PayMode = params.get("PayMode")
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filter
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        """
        :param Machines: 主机列表
        :type Machines: list of Machine
        :param TotalCount: 主机数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMalwaresRequest(AbstractModel):
    """DescribeMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 木马状态（UN_OPERATED: 未处理 | SEGREGATED: 已隔离|TRUSTED：信任）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询。
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeMalwaresResponse(AbstractModel):
    """DescribeMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 木马总数。
        :type TotalCount: int
        :param Malwares: Malware数组。
        :type Malwares: list of Malware
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Malwares = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = Malware()
                obj._deserialize(item)
                self.Malwares.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 -  查询关键字</li>
<li>Status - String - 是否必填：否 -  登录状态（NON_LOCAL_LOGIN: 异地登录 | NORMAL_LOGIN : 正常登录）</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param NonLocalLoginPlaces: 异地登录信息数组。
        :type NonLocalLoginPlaces: list of NonLocalLoginPlace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NonLocalLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = NonLocalLoginPlace()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 端口统计列表总数
        :type TotalCount: int
        :param OpenPortStatistics: 端口统计数据列表
        :type OpenPortStatistics: list of OpenPortStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPortStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self.OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self.OpenPortStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortsRequest(AbstractModel):
    """DescribeOpenPorts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Port和Uuid必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param Port: 开放端口号。Port和Uuid必填其一，使用Port表示查询该端口的列表信息。
        :type Port: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
<li>ProcessName - String - 是否必填：否 - 进程名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Port = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeOpenPortsResponse(AbstractModel):
    """DescribeOpenPorts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 端口列表记录总数。
        :type TotalCount: int
        :param OpenPorts: 端口列表。
        :type OpenPorts: list of OpenPort
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPorts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPorts") is not None:
            self.OpenPorts = []
            for item in params.get("OpenPorts"):
                obj = OpenPort()
                obj._deserialize(item)
                self.OpenPorts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics请求参数结构体

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param OnlineMachineNum: 服务器在线数。
        :type OnlineMachineNum: int
        :param ProVersionMachineNum: 专业服务器数。
        :type ProVersionMachineNum: int
        :param MalwareNum: 木马文件数。
        :type MalwareNum: int
        :param NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 暴力破解成功数。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param BaseLineNum: 安全基线数。
        :type BaseLineNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OnlineMachineNum = None
        self.ProVersionMachineNum = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.BaseLineNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.BaseLineNum = params.get("BaseLineNum")
        self.RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo请求参数结构体

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo返回参数结构体

    """

    def __init__(self):
        """
        :param PostPayCost: 后付费昨日扣费
        :type PostPayCost: int
        :param IsAutoOpenProVersion: 新增主机是否自动开通专业版
        :type IsAutoOpenProVersion: bool
        :param ProVersionNum: 开通专业版主机数
        :type ProVersionNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PostPayCost = None
        self.IsAutoOpenProVersion = None
        self.ProVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostPayCost = params.get("PostPayCost")
        self.IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self.ProVersionNum = params.get("ProVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 进程统计列表记录总数。
        :type TotalCount: int
        :param ProcessStatistics: 进程统计列表数据数组。
        :type ProcessStatistics: list of ProcessStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProcessStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self.ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self.ProcessStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProcessTaskStatusRequest(AbstractModel):
    """DescribeProcessTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeProcessTaskStatusResponse(AbstractModel):
    """DescribeProcessTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态。
<li>COMPLETE：完成（此时可以调用DescribeProcesses接口获取实时进程列表）</li>
<li>AGENT_OFFLINE：云镜客户端离线</li>
<li>COLLECTING：进程获取中</li>
<li>FAILED：进程获取失败</li>
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeProcessesRequest(AbstractModel):
    """DescribeProcesses请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Uuid和ProcessName必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param ProcessName: 进程名。Uuid和ProcessName必填其一，使用ProcessName表示，查询该进程列表信息。
        :type ProcessName: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.ProcessName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeProcessesResponse(AbstractModel):
    """DescribeProcesses返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 进程列表记录总数。
        :type TotalCount: int
        :param Processes: 进程列表数据数组。
        :type Processes: list of Process
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Processes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Processes") is not None:
            self.Processes = []
            for item in params.get("Processes"):
                obj = Process()
                obj._deserialize(item)
                self.Processes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityDynamics: 安全事件消息数组。
        :type SecurityDynamics: list of SecurityDynamic
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityDynamics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityDynamics") is not None:
            self.SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self.SecurityDynamics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 开始时间。
        :type BeginDate: str
        :param EndDate: 结束时间。
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends返回参数结构体

    """

    def __init__(self):
        """
        :param Malwares: 木马事件统计数据数组。
        :type Malwares: list of SecurityTrend
        :param NonLocalLoginPlaces: 异地登录事件统计数据数组。
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param BruteAttacks: 密码破解事件统计数据数组。
        :type BruteAttacks: list of SecurityTrend
        :param Vuls: 漏洞统计数据数组。
        :type Vuls: list of SecurityTrend
        :param BaseLines: 基线统计数据数组。
        :type BaseLines: list of SecurityTrend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Malwares = None
        self.NonLocalLoginPlaces = None
        self.BruteAttacks = None
        self.Vuls = None
        self.BaseLines = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self.BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BaseLines.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端UUID
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param UsualLoginPlaces: 常用登录地数组
        :type UsualLoginPlaces: list of UsualPlace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UsualLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self.UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self.UsualLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulInfoRequest(AbstractModel):
    """DescribeVulInfo请求参数结构体

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID。
        :type VulId: int
        """
        self.VulId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")


class DescribeVulInfoResponse(AbstractModel):
    """DescribeVulInfo返回参数结构体

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID。
        :type VulId: int
        :param VulName: 漏洞名称。
        :type VulName: str
        :param VulLevel: 漏洞等级。
        :type VulLevel: str
        :param VulType: 漏洞类型。
        :type VulType: str
        :param Description: 漏洞描述。
        :type Description: str
        :param RepairPlan: 修复方案。
        :type RepairPlan: str
        :param CveId: 漏洞CVE。
        :type CveId: str
        :param Reference: 参考链接。
        :type Reference: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.VulType = None
        self.Description = None
        self.RepairPlan = None
        self.CveId = None
        self.Reference = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.RepairPlan = params.get("RepairPlan")
        self.CveId = params.get("CveId")
        self.Reference = params.get("Reference")
        self.RequestId = params.get("RequestId")


class DescribeVulScanResultRequest(AbstractModel):
    """DescribeVulScanResult请求参数结构体

    """


class DescribeVulScanResultResponse(AbstractModel):
    """DescribeVulScanResult返回参数结构体

    """

    def __init__(self):
        """
        :param VulNum: 漏洞数量。
        :type VulNum: int
        :param ProVersionNum: 专业版机器数。
        :type ProVersionNum: int
        :param ImpactedHostNum: 受影响的专业版主机数。
        :type ImpactedHostNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulNum = None
        self.ProVersionNum = None
        self.ImpactedHostNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulNum = params.get("VulNum")
        self.ProVersionNum = params.get("ProVersionNum")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls请求参数结构体

    """

    def __init__(self):
        """
        :param VulType: 漏洞类型。
<li>WEB：Web应用漏洞</li>
<li>SYSTEM：系统组件漏洞</li>
<li>BASELINE：安全基线</li>
        :type VulType: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）

Status过滤条件值只能取其一，不能是“或”逻辑。
        :type Filters: list of Filter
        """
        self.VulType = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 漏洞数量。
        :type TotalCount: int
        :param Vuls: 漏洞列表数组。
        :type Vuls: list of Vul
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Vuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self.Vuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportBruteAttacksRequest(AbstractModel):
    """DescribeWeeklyReportBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportBruteAttacksResponse(AbstractModel):
    """DescribeWeeklyReportBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportBruteAttacks: 专业周报密码破解数组。
        :type WeeklyReportBruteAttacks: list of WeeklyReportBruteAttack
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportBruteAttacks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportBruteAttacks") is not None:
            self.WeeklyReportBruteAttacks = []
            for item in params.get("WeeklyReportBruteAttacks"):
                obj = WeeklyReportBruteAttack()
                obj._deserialize(item)
                self.WeeklyReportBruteAttacks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportInfoRequest(AbstractModel):
    """DescribeWeeklyReportInfo请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        """
        self.BeginDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")


class DescribeWeeklyReportInfoResponse(AbstractModel):
    """DescribeWeeklyReportInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyName: 账号所属公司或个人名称。
        :type CompanyName: str
        :param MachineNum: 机器总数。
        :type MachineNum: int
        :param OnlineMachineNum: 云镜客户端在线数。
        :type OnlineMachineNum: int
        :param OfflineMachineNum: 云镜客户端离线数。
        :type OfflineMachineNum: int
        :param ProVersionMachineNum: 开通云镜专业版数量。
        :type ProVersionMachineNum: int
        :param BeginDate: 周报开始时间。
        :type BeginDate: str
        :param EndDate: 周报结束时间。
        :type EndDate: str
        :param Level: 安全等级。
<li>HIGH：高</li>
<li>MIDDLE：中</li>
<li>LOW：低</li>
        :type Level: str
        :param MalwareNum: 木马记录数。
        :type MalwareNum: int
        :param NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 密码破解成功数。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyName = None
        self.MachineNum = None
        self.OnlineMachineNum = None
        self.OfflineMachineNum = None
        self.ProVersionMachineNum = None
        self.BeginDate = None
        self.EndDate = None
        self.Level = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.MachineNum = params.get("MachineNum")
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.OfflineMachineNum = params.get("OfflineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.Level = params.get("Level")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportMalwaresRequest(AbstractModel):
    """DescribeWeeklyReportMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportMalwaresResponse(AbstractModel):
    """DescribeWeeklyReportMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportMalwares: 专业周报木马数据。
        :type WeeklyReportMalwares: list of WeeklyReportMalware
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportMalwares = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportMalwares") is not None:
            self.WeeklyReportMalwares = []
            for item in params.get("WeeklyReportMalwares"):
                obj = WeeklyReportMalware()
                obj._deserialize(item)
                self.WeeklyReportMalwares.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportNonlocalLoginPlaces: 专业周报异地登录数据。
        :type WeeklyReportNonlocalLoginPlaces: list of WeeklyReportNonlocalLoginPlace
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportNonlocalLoginPlaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportNonlocalLoginPlaces") is not None:
            self.WeeklyReportNonlocalLoginPlaces = []
            for item in params.get("WeeklyReportNonlocalLoginPlaces"):
                obj = WeeklyReportNonlocalLoginPlace()
                obj._deserialize(item)
                self.WeeklyReportNonlocalLoginPlaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportVulsRequest(AbstractModel):
    """DescribeWeeklyReportVuls请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业版周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportVulsResponse(AbstractModel):
    """DescribeWeeklyReportVuls返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportVuls: 专业周报漏洞数据数组。
        :type WeeklyReportVuls: list of WeeklyReportVul
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportVuls = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportVuls") is not None:
            self.WeeklyReportVuls = []
            for item in params.get("WeeklyReportVuls"):
                obj = WeeklyReportVul()
                obj._deserialize(item)
                self.WeeklyReportVuls.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportsRequest(AbstractModel):
    """DescribeWeeklyReports请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportsResponse(AbstractModel):
    """DescribeWeeklyReports返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReports: 专业周报列表数组。
        :type WeeklyReports: list of WeeklyReport
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReports = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReports") is not None:
            self.WeeklyReports = []
            for item in params.get("WeeklyReports"):
                obj = WeeklyReport()
                obj._deserialize(item)
                self.WeeklyReports.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    * 最多只能有5个Filter
    * 同一个Filter存在多个Values，Values值数量最多不能超过5个。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class HistoryAccount(AbstractModel):
    """账号变更历史数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param Username: 帐号名。
        :type Username: str
        :param ModifyType: 帐号变更类型。
<li>CREATE：表示新增帐号</li>
<li>MODIFY：表示修改帐号</li>
<li>DELETE：表示删除帐号</li>
        :type ModifyType: str
        :param ModifyTime: 变更时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.ModifyType = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.ModifyType = params.get("ModifyType")
        self.ModifyTime = params.get("ModifyTime")


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 漏洞ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImpactedHost(AbstractModel):
    """受影响主机信息

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param LastScanTime: 最后检测时间。
        :type LastScanTime: str
        :param VulStatus: 漏洞状态。
<li>UN_OPERATED ：待处理</li>
<li>SCANING : 扫描中</li>
<li>FIXED : 已修复</li>
        :type VulStatus: str
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulId: 漏洞种类ID。
        :type VulId: int
        """
        self.Id = None
        self.MachineIp = None
        self.MachineName = None
        self.LastScanTime = None
        self.VulStatus = None
        self.Uuid = None
        self.Description = None
        self.VulId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.LastScanTime = params.get("LastScanTime")
        self.VulStatus = params.get("VulStatus")
        self.Uuid = params.get("Uuid")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")


class Machine(AbstractModel):
    """主机列表

    """

    def __init__(self):
        """
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineOs: 主机系统。
        :type MachineOs: str
        :param MachineStatus: 主机状态。
<li>OFFLINE: 离线  </li>
<li>ONLINE: 在线</li>
        :type MachineStatus: str
        :param Uuid: 云镜客户端唯一Uuid，若客户端长时间不在线将返回空字符。
        :type Uuid: str
        :param Quuid: CVM或BM机器唯一Uuid。
        :type Quuid: str
        :param VulNum: 漏洞数，非专业版将返回：0。
        :type VulNum: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param IsProVersion: 是否是专业版。
<li>true： 是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        """
        self.MachineName = None
        self.MachineOs = None
        self.MachineStatus = None
        self.Uuid = None
        self.Quuid = None
        self.VulNum = None
        self.MachineIp = None
        self.IsProVersion = None
        self.MachineWanIp = None
        self.PayMode = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachineOs = params.get("MachineOs")
        self.MachineStatus = params.get("MachineStatus")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.VulNum = params.get("VulNum")
        self.MachineIp = params.get("MachineIp")
        self.IsProVersion = params.get("IsProVersion")
        self.MachineWanIp = params.get("MachineWanIp")
        self.PayMode = params.get("PayMode")


class Malware(AbstractModel):
    """木马相关信息

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Status: 当前木马状态。
<li>UN_OPERATED：未处理</li><li>SEGREGATED：已隔离</li><li>TRUSTED：已信任</li>
<li>SEPARATING：隔离中</li><li>RECOVERING：恢复中</li>
        :type Status: str
        :param FilePath: 木马所在的路径。
        :type FilePath: str
        :param Description: 木马描述。
        :type Description: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param FileCreateTime: 木马文件创建时间。
        :type FileCreateTime: str
        :param ModifyTime: 木马文件修改时间。
        :type ModifyTime: str
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.FilePath = None
        self.Description = None
        self.MachineName = None
        self.FileCreateTime = None
        self.ModifyTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.FilePath = params.get("FilePath")
        self.Description = params.get("Description")
        self.MachineName = params.get("MachineName")
        self.FileCreateTime = params.get("FileCreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Uuid = params.get("Uuid")


class MisAlarmNonlocalLoginPlacesRequest(AbstractModel):
    """MisAlarmNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 异地登录事件Id数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class MisAlarmNonlocalLoginPlacesResponse(AbstractModel):
    """MisAlarmNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmAttributeRequest(AbstractModel):
    """ModifyAlarmAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param Attribute: 告警项目。
<li>Offline：防护软件离线</li>
<li>Malware：发现木马文件</li>
<li>NonlocalLogin：发现异地登录行为</li>
<li>CrackSuccess：被暴力破解成功</li>
        :type Attribute: str
        :param Value: 告警项目属性。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Value: str
        """
        self.Attribute = None
        self.Value = None


    def _deserialize(self, params):
        self.Attribute = params.get("Attribute")
        self.Value = params.get("Value")


class ModifyAlarmAttributeResponse(AbstractModel):
    """ModifyAlarmAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 设置自动开通状态。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NonLocalLoginPlace(AbstractModel):
    """异地登录

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Status: 登录状态
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>NORMAL_LOGIN：正常登录</li>
        :type Status: str
        :param UserName: 用户名。
        :type UserName: str
        :param City: 城市ID。
        :type City: int
        :param Country: 国家ID。
        :type Country: int
        :param Province: 省份ID。
        :type Province: int
        :param SrcIp: 登录IP。
        :type SrcIp: str
        :param MachineName: 机器名称。
        :type MachineName: str
        :param LoginTime: 登录时间。
        :type LoginTime: str
        :param Uuid: 云镜客户端唯一标识Uuid。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.MachineName = None
        self.LoginTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.MachineName = params.get("MachineName")
        self.LoginTime = params.get("LoginTime")
        self.Uuid = params.get("Uuid")


class OpenPort(AbstractModel):
    """端口列表

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        :param Port: 开放端口号。
        :type Port: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param ProcessName: 端口对应进程名。
        :type ProcessName: str
        :param Pid: 端口对应进程Pid。
        :type Pid: int
        :param CreateTime: 记录创建时间。
        :type CreateTime: str
        :param ModifyTime: 记录更新时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.Port = None
        self.MachineIp = None
        self.MachineName = None
        self.ProcessName = None
        self.Pid = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ProcessName = params.get("ProcessName")
        self.Pid = params.get("Pid")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")


class OpenPortStatistics(AbstractModel):
    """端口统计列表

    """

    def __init__(self):
        """
        :param Port: 端口号
        :type Port: int
        :param MachineNum: 主机数量
        :type MachineNum: int
        """
        self.Port = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.MachineNum = params.get("MachineNum")


class Place(AbstractModel):
    """登录地信息

    """

    def __init__(self):
        """
        :param CityId: 城市 ID。
        :type CityId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CountryId: 国家ID，暂只支持国内：1。
        :type CountryId: int
        """
        self.CityId = None
        self.ProvinceId = None
        self.CountryId = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.ProvinceId = params.get("ProvinceId")
        self.CountryId = params.get("CountryId")


class Process(AbstractModel):
    """进程信息数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param Pid: 进程Pid。
        :type Pid: int
        :param Ppid: 进程Ppid。
        :type Ppid: int
        :param ProcessName: 进程名。
        :type ProcessName: str
        :param Username: 进程用户名。
        :type Username: str
        :param Platform: 所属平台。
<li>WIN32：windows32位</li>
<li>WIN64：windows64位</li>
<li>LINUX32：Linux32位</li>
<li>LINUX64：Linux64位</li>
        :type Platform: str
        :param FullPath: 进程路径。
        :type FullPath: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Pid = None
        self.Ppid = None
        self.ProcessName = None
        self.Username = None
        self.Platform = None
        self.FullPath = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Pid = params.get("Pid")
        self.Ppid = params.get("Ppid")
        self.ProcessName = params.get("ProcessName")
        self.Username = params.get("Username")
        self.Platform = params.get("Platform")
        self.FullPath = params.get("FullPath")
        self.CreateTime = params.get("CreateTime")


class ProcessStatistics(AbstractModel):
    """进程数据统计数据。

    """

    def __init__(self):
        """
        :param ProcessName: 进程名。
        :type ProcessName: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.ProcessName = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MachineNum = params.get("MachineNum")


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马Id数组,单次最大删除不能超过200条
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessIds: 恢复成功id数组
        :type SuccessIds: list of int non-negative
        :param FailedIds: 恢复失败id数组
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SecurityDynamic(AbstractModel):
    """安全事件消息数据。

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端UUID。
        :type Uuid: str
        :param EventTime: 安全事件发生事件。
        :type EventTime: str
        :param EventType: 安全事件类型。
<li>MALWARE：木马事件</li>
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>BRUTEATTACK_SUCCESS：密码破解成功</li>
<li>VUL：漏洞</li>
<li>BASELINE：安全基线</li>
        :type EventType: str
        :param Message: 安全事件消息。
        :type Message: str
        """
        self.Uuid = None
        self.EventTime = None
        self.EventType = None
        self.Message = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Message = params.get("Message")


class SecurityTrend(AbstractModel):
    """安全趋势统计数据。

    """

    def __init__(self):
        """
        :param Date: 事件时间。
        :type Date: str
        :param EventNum: 事件数量。
        :type EventNum: int
        """
        self.Date = None
        self.EventNum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventNum = params.get("EventNum")


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马事件Id数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessIds: 隔离成功的id数组。
        :type SuccessIds: list of int non-negative
        :param FailedIds: 隔离失败的id数组。
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马Id数组，单次最大处理不能超过200条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """常用登录地

    """

    def __init__(self):
        """
        :param Id: ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param CountryId: 国家 ID。
        :type CountryId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CityId: 城市 ID。
        :type CityId: int
        """
        self.Id = None
        self.Uuid = None
        self.CountryId = None
        self.ProvinceId = None
        self.CityId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.CountryId = params.get("CountryId")
        self.ProvinceId = params.get("ProvinceId")
        self.CityId = params.get("CityId")


class Vul(AbstractModel):
    """漏洞列表数据

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID
        :type VulId: int
        :param VulName: 漏洞名称
        :type VulName: str
        :param VulLevel: 漏洞危害等级:
HIGH：高危
MIDDLE：中危
LOW：低危
NOTICE：提示
        :type VulLevel: str
        :param LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param ImpactedHostNum: 受影响机器数量
        :type ImpactedHostNum: int
        :param VulStatus: 漏洞状态
* UN_OPERATED : 待处理
* FIXED : 已修复
        :type VulStatus: str
        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.ImpactedHostNum = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.VulStatus = params.get("VulStatus")


class WeeklyReport(AbstractModel):
    """周报列表。

    """

    def __init__(self):
        """
        :param BeginDate: 周报开始时间。
        :type BeginDate: str
        :param EndDate: 周报结束时间。
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class WeeklyReportBruteAttack(AbstractModel):
    """专业周报密码破解数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Username: 被破解用户名。
        :type Username: str
        :param SrcIp: 源IP。
        :type SrcIp: str
        :param Count: 尝试次数。
        :type Count: int
        :param AttackTime: 攻击时间。
        :type AttackTime: str
        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Count = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.AttackTime = params.get("AttackTime")


class WeeklyReportMalware(AbstractModel):
    """专业周报木马数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param FilePath: 木马文件路径。
        :type FilePath: str
        :param Md5: 木马文件MD5值。
        :type Md5: str
        :param FindTime: 木马发现时间。
        :type FindTime: str
        :param Status: 当前木马状态。
<li>UN_OPERATED：未处理</li>
<li>SEGREGATED：已隔离</li>
<li>TRUSTED：已信任</li>
<li>SEPARATING：隔离中</li>
<li>RECOVERING：恢复中</li>
        :type Status: str
        """
        self.MachineIp = None
        self.FilePath = None
        self.Md5 = None
        self.FindTime = None
        self.Status = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.FilePath = params.get("FilePath")
        self.Md5 = params.get("Md5")
        self.FindTime = params.get("FindTime")
        self.Status = params.get("Status")


class WeeklyReportNonlocalLoginPlace(AbstractModel):
    """专业周报异地登录数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Username: 用户名。
        :type Username: str
        :param SrcIp: 源IP。
        :type SrcIp: str
        :param Country: 国家ID。
        :type Country: int
        :param Province: 省份ID。
        :type Province: int
        :param City: 城市ID。
        :type City: int
        :param LoginTime: 登录时间。
        :type LoginTime: str
        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Country = None
        self.Province = None
        self.City = None
        self.LoginTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.LoginTime = params.get("LoginTime")


class WeeklyReportVul(AbstractModel):
    """专业版周报漏洞数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param VulName: 漏洞名称。
        :type VulName: str
        :param VulType: 漏洞类型。
<li> WEB : WEB漏洞</li>
<li> SYSTEM :系统组件漏洞</li>
<li> BASELINE : 安全基线</li>
        :type VulType: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulStatus: 漏洞状态。
<li> UN_OPERATED : 待处理</li>
<li> SCANING : 扫描中</li>
<li> FIXED : 已修复</li>
        :type VulStatus: str
        :param LastScanTime: 最后扫描时间。
        :type LastScanTime: str
        """
        self.MachineIp = None
        self.VulName = None
        self.VulType = None
        self.Description = None
        self.VulStatus = None
        self.LastScanTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.VulStatus = params.get("VulStatus")
        self.LastScanTime = params.get("LastScanTime")