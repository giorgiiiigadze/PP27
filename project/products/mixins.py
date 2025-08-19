class QueryParamsMixin:
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            query_params = self.request.GET.copy()
            if "page" in query_params:   
                query_params.pop("page")
            context["query_params"] = query_params.urlencode()
            return context 





