# Sufy MCP Server

[Chinese Documentation](README_zh.md) | [English Documentation](README.md)

## Overview

The Model Context Protocol (MCP) Server, built based on Sufy products, enables users to access Sufy services through this MCP Server within the context of AI large model clients.

## Installation

**Prerequisites**

• Python 3.12 or higher
• UV package manager

If UV is not installed, you can install it using the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. Clone the repository:

```bash
# Clone the project and enter the directory
git clone git@github.com:sufy/sufy-mcp-server.git
cd sufy-mcp-server
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
uv pip install -e .
```

## Configuration

1. Copy the environment variable template:

```bash
cp .env.example .env
```

2. Edit the `.env` file and configure the following parameters:

```bash
# S3/Sufy authentication information
SUFY_ACCESS_KEY=your_access_key
SUFY_SECRET_KEY=your_secret_key

# Region information
SUFY_REGION_NAME=your_region
SUFY_ENDPOINT_URL=endpoint_url # eg:https://s3.your_region.sufycs.com

# Configure buckets, separate multiple buckets with commas (recommended maximum: 20 buckets)
SUFY_BUCKETS=bucket1,bucket2,bucket3
```

## Usage

### Starting the Server

1. Start in standard input/output (stdio) mode (default):

```bash
uv --directory . run sufy-mcp-server
```

2. Start in SSE mode (for web applications):

```bash
uv --directory . run sufy-mcp-server --transport sse --port 8000
```

## Development

To extend functionality, first create a new business package directory under the `core` directory (e.g., storage for storage-related features). Implement the feature extensions within this directory. Define a `load` function in the `__init__.py` file of the business package directory to register tools or resources. Finally, call this `load` function in the `__init__.py` file under the `core` directory to complete the registration of tools or resources.

```shell
core
├── __init__.py # Loads all business tools or resources
└── storage # Storage business directory
    ├── __init__.py # Loads storage tools or resources
    ├── resource.py # Storage resource extensions
    ├── storage.py # Storage utility class
    └── tools.py # Storage tool extensions
```

## Testing

### Testing with Model Control Protocol Inspector

It is highly recommended to use the [Model Control Protocol Inspector](https://github.com/modelcontextprotocol/inspector) for testing.

```shell
# Node version: v22.4.0
npx @modelcontextprotocol/inspector uv --directory . run sufy-mcp-server
```

### Testing with Cline:

Steps:

1. Install the Cline plugin in VSCode (the Cline icon will appear in the sidebar after installation).
2. Configure the large model.
3. Configure Sufy MCP:
   1. Click the Cline icon to enter the Cline plugin and select the MCP Server module.
   2. Choose "Installed," then click "Advanced MCP Settings" to configure the MCP Server. Refer to the following configuration:
   ```
   {
     "mcpServers": {
       "Sufy": {
         "command": "uv",
         "args": [
           "--directory",
           "/Users/yangsen/Workspace/App/sufy-mcp-server", # Enter the absolute path of the project directory here
           "run",
           "sufy-mcp-server"
         ],
         "env": { # Enter your Sufy MCP Server configuration here as environment variables. If downloaded from the plugin marketplace, configure here. If installed locally from source, you can also configure in the .env file as described above.
           "SUFY_ACCESS_KEY": "YOUR_ACCESS_KEY",
           "SUFY_SECRET_KEY": "YOUR_SECRET_KEY",
           "SUFY_REGION_NAME": "YOUR_REGION_NAME",
           "SUFY_ENDPOINT_URL": "YOUR_ENDPOINT_URL",
           "SUFY_BUCKETS": "YOUR_BUCKET_A,YOUR_BUCKET_B"
        },
         "disabled": false
       }
     }
   }
   ```
   3. Click the connection switch for the Sufy MCP Server to connect.
4. Create a chat window in Cline. You can now interact with the AI to use the sufy-mcp-server. Here are some examples:
    - List Sufy resource information.
    - List all buckets in Sufy.
    - List files in a specific Sufy bucket (e.g., xxx).
    - Read the content of file yyy in Sufy bucket xxx.
    - Reduce the size of image yyy in Sufy bucket xxx by 20%.