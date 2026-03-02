"""Implementations for flowsheet category tools."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from searcher.definition_searcher import DefinitionSearcher


def place_block(manager, searcher: DefinitionSearcher, session_name: str, block_name: str, block_type: str) -> str:
    """Place a new block on the flowsheet."""
    result = searcher.resolve_block_type(block_type)
    if result.matched:
        block_type = result.value
    return manager.place_block(session_name, block_name, block_type)


def remove_block(manager, session_name: str, block_name: str) -> str:
    """Remove a block from the flowsheet."""
    return manager.remove_block(session_name, block_name)


def place_stream(manager, searcher: DefinitionSearcher, session_name: str, stream_name: str, stream_type: str = "MATERIAL") -> str:
    """Place a new stream on the flowsheet."""
    result = searcher.resolve_stream_type(stream_type)
    if result.matched:
        stream_type = result.value
    return manager.place_stream(session_name, stream_name, stream_type)


def remove_stream(manager, session_name: str, stream_name: str) -> str:
    """Remove a stream from the flowsheet."""
    return manager.remove_stream(session_name, stream_name)


def connect_stream(
    manager,
    searcher: DefinitionSearcher,
    session_name: str,
    block_name: str,
    stream_name: str,
    port_name: str,
    block_type: str | None = None,
) -> str:
    """Connect a stream to a block port.(port name: F(IN), LD(OUT), B(OUT)...)"""
    if block_type:
        result = searcher.resolve_port(block_type, port_name)
        if result.matched:
            port_name = result.value
        else:
            return f"Failed to connect stream '{stream_name}' to {block_name}:{port_name}: {result.message}"
    return manager.connect_stream(session_name, block_name, stream_name, port_name)
