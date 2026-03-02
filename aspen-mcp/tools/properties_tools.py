"""Implementations for properties category tools."""

from __future__ import annotations


def get_property_method(manager, session_name: str) -> str:
    """Get the current global property method."""
    return manager.get_node_value(
        session_name, r"\Data\Properties\Specifications\Input\GOPSETNAME"
    )


def set_property_method(manager, session_name: str, method: str = "NRTL") -> str:
    """Set the global property method (e.g. NRTL, UNIQUAC, PENG-ROB, IDEAL)."""
    return manager.set_node_value(
        session_name, r"\Data\Properties\Specifications\Input\GOPSETNAME", method
    )


def add_component(manager, session_name: str, component_id: str) -> str:
    """Add a component to the simulation component list."""
    return manager.add_component(session_name, component_id)
