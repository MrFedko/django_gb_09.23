from django.views.generic import TemplateView
import random
import logging

logger = logging.getLogger(__name__)


class CoinView(TemplateView):
    template_name = 'randomizer/coin.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['coin_side'] = random.choice(['орёл', 'решка'])
        logger.info(f'результат: {contex["coin_side"]}')
        return contex


class CubeView(TemplateView):
    template_name = 'randomizer/cube.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['cube_name'] = random.randint(1, 6)
        logger.info(f'результат: {contex["cube_name"]}')
        return contex


class NumberView(TemplateView):
    template_name = 'randomizer/number.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['number'] = random.randint(1, 100)
        logger.info(f'результат: {contex["number"]}')
        return contex
