"""Competition and round lifecycle plugin for MEDUSA."""

from flask import jsonify, render_template_string


def _round_payload():
    return {
        "plugin": "medusa_lifecycle",
        "status": "online",
        "version": "0.1.0",
        "current_round": "Round 3",
        "state": "active",
        "start_time": "2026-10-06T18:00:00Z",
        "end_time": "2026-10-08T18:00:00Z",
        "rounds": [
            {"id": 1, "name": "Qualification", "status": "complete"},
            {"id": 2, "name": "Operational Sprint", "status": "complete"},
            {"id": 3, "name": "Final Engagement", "status": "active"},
        ],
    }


def load(app):
    @app.route("/admin/plugins/medusa-lifecycle", methods=["GET"])
    def medusa_lifecycle_admin_view():
        return render_template_string(
            """
            <h1>MEDUSA Lifecycle Control</h1>
            <p>Manage competition state, round transitions, and challenge windows.</p>
            <ul>
                <li>Round orchestration</li>
                <li>Competition state management</li>
                <li>Operational timing control</li>
            </ul>
            """
        )

    @app.route("/api/v1/medusa/lifecycle/status", methods=["GET"])
    def medusa_lifecycle_status():
        return jsonify(_round_payload())

    @app.route("/medusa-lifecycle", methods=["GET"])
    def medusa_lifecycle_public_view():
        return render_template_string(
            """
            <html>
                <head><title>MEDUSA Lifecycle</title></head>
                <body>
                    <h1>Competition and Round Lifecycle</h1>
                    <p>Exercise control of challenge timing, competition windows, and operational transitions.</p>
                </body>
            </html>
            """
        )

    return app
