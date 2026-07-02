from app import app


def test_layout_exists():
    assert app.layout is not None


def test_header_exists():
    layout_str = str(app.layout)
    assert "Soul Foods Sales Visualiser" in layout_str


def test_graph_exists():
    layout_str = str(app.layout)
    assert "line-chart" in layout_str