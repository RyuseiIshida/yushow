import pandas as pd

def get_document(query):
    GET_URL = 'http://resource.ufocatch.com/atom/edinet/query/' + query


def get_edinet_code(company_name):
    # 検索システム 部分一致でEDINETコードリストを返す
    df_company_name = pd.read_csv('assets/EdinetcodeDlInfo.csv')
    df_company_name = df_company_name.query('提出者名.str.contains(\"' + company_name + '\")', engine='python')
    return df_company_name['ＥＤＩＮＥＴコード'].values


def get_company_name(edinet_code):
    df_edinet_code = pd.read_csv('assets/EdinetcodeDlInfo.csv', index_col='ＥＤＩＮＥＴコード')
    return df_edinet_code.at[edinet_code, '提出者名']


def get_company_name_list(edinet_codes):
    df_edinet_code = pd.read_csv('assets/EdinetcodeDlInfo.csv', index_col='ＥＤＩＮＥＴコード')
    company_name_list = [df_edinet_code.at[ecode, '提出者名'] for ecode in edinet_codes]
    return company_name_list


if __name__ == '__main__':
    print(get_edinet_code('マネーフォワード'))
    # And(get_company_name(['E31084','E34920','E27799']))
    code = get_edinet_code('マネ')
    print(get_company_name_list(code))
