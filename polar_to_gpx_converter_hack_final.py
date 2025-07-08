import json
import gpxpy
import gpxpy.gpx
import dateutil.parser
import os
import unidecode

# Directory to convert
DIRECTORY_IN = '.\\polar-user-data-export\\'
file_list = os.listdir(DIRECTORY_IN)

# Directory to write to
DIRECTORY_OUT = '.\\converted_polar-user-data-export\\'
if not os.path.exists(DIRECTORY_OUT): os.mkdir(DIRECTORY_OUT)

# Resample gps track to include only every nth point (n = integer).
# Leave resample_number = 1 to include the whole track.
resample_number = 10

for file in file_list:
   if not file.startswith('training-session'): continue # Export .zip contains files other than training sessions.
   print('------------')
   print(file)
   # Read json file
   file_path_in = os.path.join(DIRECTORY_IN,file)
   json_file = json.load(open(file_path_in,'rb'))
   
   # Get relevant data
   exercise = json_file['exercises'][0]
   if not 'sport' in exercise.keys(): sport = 'NOT_DEFINED'
   else: sport = exercise['sport']
   if not 'note' in json_file.keys(): own_note = 'no note available'
   else: own_note = json_file['note']
   samples = json_file['exercises'][0]['samples']
   if not 'recordedRoute' in samples:
      print('No GPS track in file. Continuing to next file...')
      continue
   recorded_route = samples['recordedRoute']
   recorded_route = recorded_route[::resample_number]
   

   # New output file name and check if it already exists
   new_file_name = sport + '_' + os.path.splitext(file)[0] + '.gpx'
   file_path_out = os.path.join(DIRECTORY_OUT,new_file_name)
   if os.path.exists(file_path_out):
      print('This file has already been processed! Continuing to next file...')
      continue

   # To GPX format
   gpx = gpxpy.gpx.GPX()
   gpx.keywords = sport
   gpx.description = unidecode.unidecode(own_note) # Takes care of umlauts that cause troubles for visualization.
   gpx_track = gpxpy.gpx.GPXTrack()
   gpx.tracks.append(gpx_track)
   gpx_segment = gpxpy.gpx.GPXTrackSegment()
   gpx_track.segments.append(gpx_segment)
   
   # Append all track points
   for row in recorded_route:
      gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(row['latitude'],
                                                               row['longitude'],
                                                               elevation = row['altitude'],
                                                               time = dateutil.parser.parse(row['dateTime'])))
   # Write to file
   xml_formatting = gpx.to_xml()
   with open(file_path_out, "w") as f:
    f.write(gpx.to_xml())
   print('------------')
