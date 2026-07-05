"""SDR Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_qualify_inbound():
    """Test Qualify an inbound lead and determine next action."""
    tools = AgentTools()
    result = await tools.qualify_inbound(lead_data="test", qualification_framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_book_meeting():
    """Test Book a meeting between a qualified prospect and an AE."""
    tools = AgentTools()
    result = await tools.book_meeting(prospect_id="test", ae_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_handle_objection():
    """Test Generate objection handling response for a common sales objection."""
    tools = AgentTools()
    result = await tools.handle_objection(objection="test", context="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_follow_up():
    """Test Generate and schedule follow-up message for a prospect."""
    tools = AgentTools()
    result = await tools.follow_up(prospect_id="test", previous_interaction="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.sdr_agent_agent import SdrAgentAgent
    agent = SdrAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
