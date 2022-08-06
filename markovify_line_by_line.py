import markovify
from corus import load_lenta

path = 'lenta_1000.csv.gz'
records = load_lenta(path)
combined_model = None
n = 0

for record in records:
    text = record.text
    # print(text)
    model = markovify.Text(text, retain_original=False, well_formed=False)
    if combined_model:
        combined_model = markovify.combine(models=[combined_model, model])
    else:
        combined_model = model
    n += 1
    if n % 100 == 0:
        print(n)
    # print(record.text)

for i in range(10):
    print()
    print(combined_model.make_short_sentence(280))
