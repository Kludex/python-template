from copier_templates_extensions import ContextHook
from typing import Any
import datetime


class ContextUpdater(ContextHook):
    update = False

    def hook(self, context: dict[str, Any]) -> dict[str, Any]:  # type: ignore
        project_name = context["project_name"]
        project_slug = context["project_slug"] = project_name.lower().replace(" ", "-")
        context["package"] = project_slug.replace("-", "_")
        context["__year"] = str(datetime.datetime.today().year)
