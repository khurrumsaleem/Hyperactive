"""Base class for optimizer."""
# copyright: hyperactive developers, MIT License (see LICENSE file)

from skbase.base import BaseObject


class BaseOptimizer(BaseObject):
    """Base class for optimizer."""

    _tags = {
        "object_type": "optimizer",
        "python_dependencies": None,
    }

    def __init__(self):
        super().__init__()
        assert hasattr(self, "experiment"), "Optimizer must have an experiment."
        search_config = self.get_params()
        self._experiment = search_config.pop("experiment", None)

    def get_search_config(self):
        """Get the search configuration.

        Returns
        -------
        dict with str keys
            The search configuration dictionary.
        """
        search_config = self.get_params(deep=False)
        search_config.pop("experiment", None)
        return search_config

    def get_experiment(self):
        """Get the experiment.

        Returns
        -------
        BaseExperiment
            The experiment to optimize parameters for.
        """
        return self._experiment

    def run(self):
        """Run the optimization search process.

        Returns
        -------
        best_params : dict
            The best parameters found during the optimization process.
        """
        experiment = self.get_experiment()
        search_config = self.get_search_config()

        best_params = self._run(experiment, **search_config)
        self.best_params_ = best_params
        return best_params
