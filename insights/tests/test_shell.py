from unittest.mock import patch

from insights import make_pass
from insights.shell import Models


def fake_rule():
    pass


def test_show_rule_report_pages_the_report():
    broker = {fake_rule: make_pass("FAKE_RULE_PASS")}
    models = Models(broker, {}, "", "", False)
    with patch("insights.shell.plugins.is_rule", return_value=True), \
            patch("insights.shell.render", return_value="rule body"), \
            patch("insights.shell.render_links", return_value=""), \
            patch("insights.shell.IPython.core.page.page") as page:
        models.show_rule_report()
    output = page.call_args[0][0]
    assert "fake_rule" in output
    assert "rule body" in output
