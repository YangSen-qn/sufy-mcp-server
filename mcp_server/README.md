#  Sufy MCP 服务器

基于 Sufy 产品构建的 Model Context Protocol (MCP) 服务器，支持在 AI 大模型的上下文中直接访问和操作 Sufy 的服务。

## Tools

### 存储工具

1. `ListBuckets`
   - 查询当前用户配置的 Bucket 
   - Inputs:
     - `prefix` (string, optional): Bucket 名称前缀，用于筛选特定前缀的 Bucket 
   - Returns:
     - 满足条件的 Bucket 列表及其详细信息

2. `ListObjects`
   - 列举指定 Bucket 中的文件列表
   - Inputs:
     - `bucket` (string): Bucket 名称
     - `max_keys` (integer, optional): 单次返回的最大文件数量，默认为20，最大值为100
     - `prefix` (string, optional): 文件 Key 前缀，用于筛选特定前缀的文件
     - `start_after` (string, optional): 起始标记，指定列表的开始位置，可以是上一次列举的结果中最后一个文件的 Key
   - Returns:
     - 满足条件的文件列表及其详细信息

3. `GetObject`
   - 获取 Bucket 中文件的内容
   - Inputs:
     - `bucket` (string):  Bucket 名称
     - `key` (string): 文件的 Key
   - Returns:
     - 文件内容

4. `GetObjectURL`
   - 生成文件的访问链接
   - Inputs:
     - `bucket` (string):  Bucket 名称
     - `key` (string): 文件的 Key
     - `disable_ssl` (boolean, optional): 是否禁用 HTTPS，默认使用 HTTPS
     - `expires` (integer, optional): 链接有效期，单位为秒
   - Returns:
     - 对象的访问链接

### 图片处理工具

1. `ImageScaleByPercent`
   - 按照指定百分比缩放图片
   - Inputs:
     - `object_url` (string): 待处理图片的访问链接，图片必须存储在 Sufy 空间中
     - `percent` (integer): 缩放比例，范围为1%~999%
   - Returns:
     - `object_url`: 处理后图片的访问链接

2. `ImageScaleBySize`
   - 按照指定宽度或高度缩放图片
   - Inputs:
     - `object_url` (string): 待处理图片的访问链接，图片必须存储在 Sufy 空间中
     - `width` (integer, optional): 目标宽度，单位为像素
     - `height` (integer, optional): 目标高度，单位为像素
   - 注意：至少需要指定宽度或高度中的一个参数
   - Returns:
     - `object_url`: 处理后图片的访问链接

3. `ImageBlur`
   - 为图片添加高斯模糊效果
   - Inputs:
     - `object_url` (string): 待处理图片的访问链接，图片必须存储在 Sufy 空间中
     - `radius` (string, optional): 模糊半径，取值范围为1-200
     - `sigma` (string, optional): 正态分布的标准差，值必须大于0
   - 注意：如果只指定一个参数，另一个参数将自动使用相同的值
   - Returns:
     - `object_url`: 处理后图片的访问链接

### 其他工具

1. `Version`
   - 获取 Sufy MCP Server 的版本信息
   - Inputs: 无
   - Returns:
     - 服务器版本信息




