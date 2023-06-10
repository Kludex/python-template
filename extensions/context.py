from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context):
        project_name: str = context["project_name"]
        context["project_slug"] = project_name.lower().replace(" ", "-")
        context["package"] = project_name.lower().replace(" ", "_")
        return context
