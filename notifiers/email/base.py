from abc import abstractmethod, ABC


class BaseEmailNotifier(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def notify(self):
		pass

	@abstractmethod
	def prepare_message(self):
		pass
