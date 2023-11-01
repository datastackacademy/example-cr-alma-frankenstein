#!/bin/bash
gsutil -m cp gs://data.datastack.academy/spotify/spotify_artists.csv .
gsutil -m cp gs://data.datastack.academy/spotify/*json .
