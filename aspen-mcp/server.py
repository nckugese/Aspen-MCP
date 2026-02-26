from mcp.server.fastmcp import FastMCP
from aspen_manager import AspenPlusManager

mcp = FastMCP(name="aspen-plus")
manager = AspenPlusManager()


@mcp.tool()
def open_aspen_plus(file_path: str) -> str:
    """Open Aspen Plus and load a .bkp simulation file.

    Args:
        file_path: Path to the .bkp file.
    """
    return manager.open_with_file(file_path)


@mcp.tool()
def close_aspen_plus(session_name: str = None) -> str:
    """Close an Aspen Plus session.

    Args:
        session_name: Name of the session to close (e.g. 'Simulation 1'). If not provided, closes all sessions.
    """
    return manager.close(session_name)


@mcp.tool()
def list_aspen_sessions() -> str:
    """List all active Aspen Plus sessions."""
    return manager.list_sessions()


if __name__ == "__main__":
    mcp.run()
