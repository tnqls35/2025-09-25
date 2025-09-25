

import streamlit as st
import math

st.title('순열과 조합 경우의 수 계산기')

option = st.radio('계산할 항목을 선택하세요', ['순열', '조합'])

import itertools

if option == '순열':
    st.markdown('**서로 다른 n개 중 r개를 나열합니다.**')
    col1, col2 = st.columns(2)
    n = col1.number_input('n (전체 개수)', min_value=0, value=5, step=1)
    r = col2.number_input('r (나열할 개수)', min_value=0, value=3, step=1)
    if st.button('나열한다'):
        if n < r:
            st.error('경우의 수를 구할 수 없습니다.\n이유: 전체 개수(n)보다 뽑거나 나열할 개수(r)가 더 많으면, 실제로 선택할 수 있는 대상이 부족하므로 경우의 수가 정의되지 않습니다.')
        else:
            result = math.perm(n, r) if hasattr(math, 'perm') else math.factorial(n) // math.factorial(n - r)
            st.success(f'서로 다른 {n}개 중 {r}개를 나열하는 경우의 수: {result}')
            perms = list(itertools.permutations(range(n), r))
            st.markdown('**모든 순열 리스트**')
            for i, perm in enumerate(perms, 1):
                st.write(f'{i}: {[j+1 for j in perm]}')

elif option == '조합':
    st.markdown('**서로 다른 n개 중 r개를 뽑습니다.**')
    col1, col2 = st.columns(2)
    n = col1.number_input('n (전체 개수)', min_value=0, value=5, step=1, key='comb_n')
    r = col2.number_input('r (뽑을 개수)', min_value=0, value=3, step=1, key='comb_r')
    if st.button('뽑는다'):
        if n < r:
            st.error('경우의 수를 구할 수 없습니다.\n이유: 전체 개수(n)보다 뽑을 개수(r)가 더 많으면, 실제로 선택할 수 있는 대상이 부족하므로 경우의 수가 정의되지 않습니다.')
        else:
            result = math.comb(n, r) if hasattr(math, 'comb') else math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
            st.success(f'서로 다른 {n}개 중 {r}개를 뽑는 경우의 수: {result}')
            combs = list(itertools.combinations(range(n), r))
            st.markdown('**모든 조합 리스트**')
            for i, comb in enumerate(combs, 1):
                st.write(f'{i}: {[j+1 for j in comb]}')