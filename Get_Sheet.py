import requests
import bs4
import pandas as pd


def get_sheet(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/123.0.0.0 Safari/537.36",
        # "cookies": "RK=V434Cmvsa+; ptcz=c38345c2a0ac903e81e0b66ed6183e684c52493afc92639f9461256a8efab698; fingerprint=d78fe1d7b9f148e8bed0cc958d68f11438; pgv_pvid=4883930122; low_login_enable=1; uid=144115384085642378; env_id=gray-no4; gray_user=true; DOC_SID=6377c52987a649129950f2d25ea86351fd1f14e3dc3149a28f9f00a0cd32f683; SID=6377c52987a649129950f2d25ea86351fd1f14e3dc3149a28f9f00a0cd32f683; loginTime=1711968690337; optimal_cdn_domain=docs2.gtimg.com; backup_cdn_domain=docs2.gtimg.com; traceid=da71f96e23; hashkey=da71f96e; _clck=nzdmts|1|fl0|0; pgv_info=ssid=s1713350125305361; go_session_id=NTM1ZGY5MTQtY2E4MC00YjcyLTk1OWUtNTU3ODA5ODA0NWQ2.d897815d3dbb785209a448409097d7a5c76f08ae; _qpsvr_localtk=0.8403637184077992; uid_key=EOP1mMQHGixLTG5iM2xEeFJsNXpvcytyRzFVQUZub2JUVFJxY1BjRzd4cEYxdEN2Q29FPSKBAmV5SmhiR2NpT2lKQlEwTkJURWNpTENKMGVYQWlPaUpLVjFRaWZRLmV5SlVhVzU1U1VRaU9pSXhORFF4TVRVek9EUXdPRFUyTkRJek56Z2lMQ0pXWlhJaU9pSXhJaXdpUkc5dFlXbHVJam9pYzJGaGMxOTBiMk1pTENKU1ppSTZJa2RyV0V0M2J5SXNJbVY0Y0NJNk1UY3hOVGswTkRBek1Dd2lhV0YwSWpveE56RXpNelV5TURNd0xDSnBjM01pT2lKVVpXNWpaVzUwSUVSdlkzTWlmUS52LWZaS1FVQW1KLVdQaXJTNVhMNDdtZVNwd0dWU0RtTjc4Mm13a3I5dUMwKN70nLIG; wx_appid=wxd45c635d754dbf59; openid=oDzL40N7OWePGNkeTOXnmEejHK9Y; access_token=79_maZz5zWV2bwhk54MgCkh6icVMEmTnosMcNJsly-WDXvKMGgUycVsyQc6VAw1e2bZbtK3Xi-b-q7aJA1EOahtlXbeMK_SAWcDqsF5F0lqFbI; refresh_token=79_AqWExL54aHlb-1hYw3vzdpdcriTpYdR7kImPeRnrS2ZpKsk5rKK5RSfEc9yLeuO00KffyVjxzFW6q4cLaPqiLWGHf32fPH8pZWrg85b6bCg; has_been_login=1; utype=wx; TOK=a5d75ac9feab1a23",
        # "Referer": "https://docs.qq.com/sheet/DTVVkaEFZV0ZrQVhv?tab=o1b2n0",
        # "Content-Type": "application/json"

    }

    response = requests.get(url, headers=headers)

    df = pd.read_html(response.text, header=1, index_col=0)[0]

    print(df)

    # content = response.text
    # if response.ok:
    #     print(response.content)
    # else:
    #     print("请求失败!\nHTTP状态码为:" + str(response.status_code))


if __name__ == '__main__':
    get_sheet("https://docs.qq.com/sheet/DS21hcmNVYnlmaWZ6?tab=7gr117")
