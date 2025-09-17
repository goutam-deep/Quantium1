import pytest

# `dash_duo` is the Dash test fixture provided by dash[testing]
def test_header_is_present(dash_duo):
    from app import app   # Import your Dash app instance

    dash_duo.start_server(app)

    # Look for header element (assuming it has id="header")
    header = dash_duo.find_element("#header")
    assert header is not None
    assert "Dashboard" in header.text  # Adjust text to match your header

def test_visualization_is_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    # Look for graph (assuming it has id="main-graph")
    graph = dash_duo.find_element("#main-graph")
    assert graph is not None

def test_region_picker_is_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    # Look for dropdown (assuming it has id="region-picker")
    region_picker = dash_duo.find_element("#region-picker")
    assert region_picker is not None
