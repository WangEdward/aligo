"""Other"""

from aligo.core import *
from aligo.core.Config import ADRIVE_V1_USER_ALBUMS_INFO
from aligo.request import *
from aligo.response import *
from aligo.types import BaseDrive


class Other(Core):
    """Other"""

    def get_path(self, file_id: str, drive_id: str = None) -> GetFilePathResponse:
        """
        官方：获取文件（夹）目录信息
        :param file_id: 文件（夹）ID
        :param drive_id: 文件（夹）所在网盘ID
        :return: [GetFilePathResponse]

        用法示例：
        >>> from aligo import Aligo, BaseFile, GetFilePathResponse
        >>> aligo = Aligo()
        >>> file_path_info = aligo.get_path('60f927edf4c9f64d3a0c4704b80154cfa3d13c2a')
        >>> assert isinstance(file_path_info, GetFilePathResponse)
        >>> for item in file_path_info.items:
        >>>     assert isinstance(item, BaseFile)
        """
        body = GetFilePathRequest(file_id=file_id, drive_id=drive_id)
        return self._core_get_path(body)

    def get_albums_info(self):
        response = self._post(ADRIVE_V1_USER_ALBUMS_INFO)
        data = response.json()['data']
        return BaseDrive(drive_id=data.get('driveId'), drive_name=data.get('driveName'))
