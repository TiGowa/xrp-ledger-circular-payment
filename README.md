# How profitable is the circular payment strategy?

Although it is possible to send XRP to yourself, from wallet A to wallet B (as long as you own both wallets), it is impossible to consume exciting offer(s) on the ledger by sending XRP from one wallet to another. In other words, an XRP-to-XRP transaction does not use any paths. 

However, it looks like rMHSvqV83BhFDhkQtXELxNYyyhq776dhzG managed to find a workaround/ way to send an issued currency or IOU (I Owe You, basically a debt instrument) to itself, while consuming exciting offer(s) on the Ledger, therefore taking advantage of arbitrage opportunities.

Example: USD.Bob-->XRP-->CNY.Yua-->XRP-->EUR.Joe-->USD.Bob

The wallet rMHSvqV83BhFDhkQtXELxNYyyhq776dhzG created 9 issued currencies or IOUs. The individual or group of individuals operating the wallet then created 9 sub wallets, each one setting/ having a trust line with one IOU: UPD, UPY, UPC, UPK, UPH, UPE, UPA, UPU, UPO.

Each so-called "sub" wallet is designed to send recurrent payments of IOU to the so-called "master" wallet (rMHSvqV83BhFDhkQtXELxNYyyhq776dhzG). Each payment has a Limit Quality specification, meaning that the payment is triggered only and only if it does respect a specific XRP/IOU "quality" ratio.

_The XRP Ledger defines the "quality" of a currency exchange as the ratio of the numeric amount in to the numeric amount out. For example, if you spend $2 USD to receive £1 GBP, then the "quality" of that exchange is 0.5._

I briefly studied the evolution of the XRP balances corresponding to each sub wallet: UPD, UPY, UPC, UPK, UPH, UPE, UPA, UPU, UPO. I added a virtual aggregate wallet (red line).

Time period: 14-01-2019 to 13-01-2020

Two takeaways:
- The strategy generated a net profit of ~ 10,000 XRP in one year.
- Two phases are visible/ distinguishable. My assumption is that before June 2019, the strategy/ project was probably in a test mode. At the beginning of June, all sub wallets were initialised with more or less the same amount of xrp. Then the strategy has been running with consistency.

![Alt text](https://raw.githubusercontent.com/TiGowa/xrp-ledger-circular-payment/master/graph.png?raw=true "Optional Title")
