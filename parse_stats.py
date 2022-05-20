from collections import defaultdict

with open('stats.csv') as f:
    lines = f.readlines()

time = None
stats = defaultdict(dict)
times = list()
for line in lines:
    line = line.strip()
    if line == '--,0.00%,0B / 0B':
        continue
    columns = line.split(',')
    if len(columns) == 1:
        [time] = columns
        times.append(time)
    else:
        name, cpu, mem = columns
        if name.startswith('python-pgbouncer-benchmark_test'):
            continue
        name = name.removeprefix('python-pgbouncer-benchmark-')
        name = name.removesuffix('-1')
        mem = mem.split('/')[0].strip().removesuffix('MiB').replace('.', ',')
        cpu = cpu.strip().removesuffix('%').replace('.', ',')
        stats[name][time] = (cpu, mem)

times = times[:-1]

text = 'name;' + ';'.join(times)
text += '\n'
for name in stats:
    text += name
    for time in times:
        text += ';' + stats[name][time][0]
    text += '\n'

text += '\n'
text += 'name;' + ';'.join(times)
text += '\n'
for name in stats:
    text += name
    for time in times:
        text += ';' + stats[name][time][1]
    text += '\n'

print(text)
