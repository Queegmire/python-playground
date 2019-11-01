from functools import partial


def html_list(items, *, ordered=True):
	inner = '\n'.join(f'\t<li>{item}</li>' for item in items)
	outer = 'ol' if ordered else 'ul'
	return f'<{outer}>\n{inner}\n</{outer}'

ordered_list = partial(html_list, ordered=True)
unordered_list = partial(html_list, ordered=False)

items = ['one', 'two', 'three']
print(ordered_list(items))
print()
print(unordered_list(items))
