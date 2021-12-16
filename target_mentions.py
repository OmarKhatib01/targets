from targets import popDict
import csv

file = csv.reader(open('data.csv', 'r'))
targets = popDict(file)


def check_target(targets, label, text, target_mentions):
  """
  targets: a list of all possible spellings of the target mention
  label: Choose an informative label for each target, please follow the same style as the examples below
  """
  if any(substring in text for substring in targets):
        target_mentions.append(label)

for key in targets:
    check_target([key, targets[key].fn+" "+targets[key].ln, targets[key].fn+targets[key].ln], text, target_mentions)
    # need to change text and target mentions attribute to something that exists