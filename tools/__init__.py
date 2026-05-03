"""Five passive-OSINT tools wired behind a uniform Tool interface.

All tools take a ``target`` string (typically a domain) and return a
:class:`tools.base.ToolResult` whose ``findings`` list contains
:class:`memory.evidence.Evidence` objects.

By design, every tool here is *read-only* against publicly accessible
endpoints. None of them log in, scan ports, or send anything other than
the canonical query advertised in the OSINT toolbox.
"""
from tools.base import Tool, ToolResult, ToolError
from tools.whois_tool import WhoisTool
from tools.dns_tool import DnsTool
from tools.shodan_tool import ShodanTool
from tools.github_dork_tool import GitHubDorkTool
from tools.wayback_tool import WaybackTool

__all__ = [
    "Tool", "ToolResult", "ToolError",
    "WhoisTool", "DnsTool", "ShodanTool", "GitHubDorkTool", "WaybackTool",
]


def all_tools() -> list[Tool]:
    """Canonical tool order — matches the prompt and the scorecard."""
    return [
        WhoisTool(),
        DnsTool(),
        ShodanTool(),
        GitHubDorkTool(),
        WaybackTool(),
    ]
