"""University and team management plugin for MEDUSA."""

from flask import jsonify, render_template_string


def _team_payload():
    return {
        "plugin": "medusa_university",
        "status": "online",
        "version": "0.1.0",
        "teams": [
            {"id": 1, "name": "Blue Team", "institution": "North Campus", "score": 4300},
            {"id": 2, "name": "Red Team", "institution": "East Campus", "score": 4150},
            {"id": 3, "name": "White Team", "institution": "South Campus", "score": 3980},
        ],
    }


def load(app):
    @app.route("/admin/plugins/medusa-university", methods=["GET"])
    def medusa_university_admin_view():
        return render_template_string(
            """
            <h1>MEDUSA University Ops</h1>
            <p>Manage institutional teams, operations windows, and competition participation.</p>
            <ul>
                <li>Team roster management</li>
                <li>Institutional scoring sync</li>
                <li>Event scheduling and participation windows</li>
            </ul>
            """
        )

    @app.route("/api/v1/medusa/university/teams", methods=["GET"])
    def medusa_university_teams():
        return jsonify(_team_payload())

    @app.route("/medusa-university", methods=["GET"])
    def medusa_university_public_view():
        return render_template_string(
            """
            <html>
                <head><title>MEDUSA University</title></head>
                <body>
                    <h1>University and Team Management</h1>
                    <p>Secure event administration for university teams and institutional participation.</p>
                </body>
            </html>
            """
        )

    return app
