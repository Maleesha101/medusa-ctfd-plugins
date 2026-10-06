"""MEDUSA Core bootstrap plugin for CTFd.

This plugin follows the standard CTFd plugin contract: a `load(app)` function is
required so CTFd can register hooks, routes, and admin UI extensions without
modifying the upstream codebase.
"""

from flask import jsonify, render_template_string


def _medusa_status_payload():
    return {
        "plugin": "medusa_core",
        "name": "MEDUSA Core",
        "status": "online",
        "version": "0.1.0",
        "features": [
            "competition_lifecycle",
            "ops_dashboard",
            "scoreboard_hooks",
            "plugin_bootstrap",
        ],
    }


def load(app):
    """Register MEDUSA plugin routes and admin UI hooks with the CTFd app."""

    @app.route("/admin/plugins/medusa-core", methods=["GET"])
    def medusa_core_admin_view():
        return render_template_string(
            """
            <h1>MEDUSA Core</h1>
            <p>Cyber operations control plane for the CTFd competition environment.</p>
            <ul>
                <li>Competition lifecycle orchestration</li>
                <li>Operational telemetry</li>
                <li>Team and challenge status integration</li>
            </ul>
            """
        )

    @app.route("/api/v1/medusa/core/status", methods=["GET"])
    def medusa_core_status():
        return jsonify(_medusa_status_payload())

    @app.route("/medusa-core", methods=["GET"])
    def medusa_core_public_view():
        return render_template_string(
            """
            <html>
                <head>
                    <title>MEDUSA Core</title>
                </head>
                <body>
                    <h1>MEDUSA Core</h1>
                    <p>Secure command-and-control experience for challenge operations.</p>
                </body>
            </html>
            """
        )

    return app
