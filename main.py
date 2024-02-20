from aiogram import Bot, Dispatcher, executor, types
import python_weather
import config


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
client = python_weather.Client(unit=python_weather.METRIC)


@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)

    response = f'{weather.nearest_area.name}, {weather.nearest_area.country}\n'
    response += f'Today is {weather.current.description.lower()}\n'
    response += f'Current temperature: {weather.current.temperature}°C\n'

    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
