"""Display the calculator user interface."""
from calculator_view import CalculatorView
from calculator_controller import CalculatorController
from calculator_model import CalculatorModel


if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    view = CalculatorView()
    model = CalculatorModel(view)
    controller = CalculatorController(model, view)
    view.mainloop()
