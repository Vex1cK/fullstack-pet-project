import { Card } from "antd"

function CryptocurrencyCard(props) {
  const { currency } = props

  const price = currency.quote.USD.price.toLocaleString('ru-RU', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
  const capitalisation = currency.quote.USD.market_cap.toLocaleString('ru-RU', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
  const daily_change_percent = currency.quote.USD.percent_change_24h.toFixed(2)

  return (
    <>
      <Card
        title={
          <div className="flex items-center gap-3">
            <img src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`} />
            <span>{currency.name}</span>
          </div>
        }
        style={{ width: 350 }}>
        <p>Текущая цена: {price}$</p>
        <p>Изменение цены за 24 часа: <span
          className={
            daily_change_percent > 0
              ? "text-green-500"
              : daily_change_percent < 0
                ? "text-red-500"
                : "text-gray-700"
          }
        >
          {daily_change_percent > 0
            ? `+${daily_change_percent}%`
            : daily_change_percent < 0
              ? `${daily_change_percent}%`
              : `+0%`}
        </span></p>
        <p>Текущая капитализация: {capitalisation}$</p>
      </Card>
    </>
  )
}

export default CryptocurrencyCard
