meter_per_people_number, area = map(int, input().split())
news_people_number_1, news_people_number_2, news_people_number_3, news_people_number_4, news_people_number_5 = map(int, input().split())

exact_people_number = meter_per_people_number*area
print(news_people_number_1-exact_people_number, news_people_number_2-exact_people_number, news_people_number_3-exact_people_number, news_people_number_4-exact_people_number, news_people_number_5-exact_people_number)
