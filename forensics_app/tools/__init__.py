"""Register course functionality here so it appears in the sidebar."""

from .channel_split import ChannelSplitTool
from .grayscale import GrayscaleTool
from .image_info import ImageInfoTool
from .registry import ToolRegistry
from .channel_swap import (
    SwapGreenBlueTool,
    SwapRedBlueTool,
    SwapRedGreenTool,
)
from .histogram import GrayscaleHistogramTool,RGBHistogramsTool

def build_tool_registry() -> ToolRegistry:
    return ToolRegistry(
        [
            ImageInfoTool(),
            ChannelSplitTool(),
            GrayscaleTool(),
        ]
    )


__all__ = ["ToolRegistry", "build_tool_registry"]
