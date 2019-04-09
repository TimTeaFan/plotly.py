import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='size',
        parent_name='layout.xaxis.title.font',
        **kwargs
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'ticks'),
            min=kwargs.pop('min', 1),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )