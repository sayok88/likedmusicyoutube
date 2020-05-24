# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from time import sleep

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    # How to create cred https://stackoverflow.com/a/52222827/2138792
    client_secrets_file = "client_secret_866116146487-aftoa9qtv3taf2vdqu7ovqdh1an33fdh.apps.googleusercontent.com.json"
    playlistId = 'PLozlHB3ta93E7zSsknIEBNpYd_FhQXCbE'
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    def getplaylistvids(pid):
        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId="LM"
        )
        response = request.execute()
        if 'pageInfo' in response:
            pageInfo = response['pageInfo']
            if 'totalResults' in pageInfo:
                maxResults = pageInfo['totalResults']

        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=pid,
            maxResults=50 if maxResults > 50 else maxResults
        )
        response = request.execute()
        print(response)
        vids = []
        nextPageToken = response['nextPageToken']
        if 'items' in response:
            items = response['items']
            for item in items:
                if "contentDetails" in item:
                    vids.append(item['contentDetails']['videoId'])
        while len(vids) < maxResults:
            sleep(1)
            request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=pid,
                maxResults=50,
                pageToken=nextPageToken
            )
            response = request.execute()
            print(response)

            if 'items' in response:
                items = response['items']
                for item in items:
                    if "contentDetails" in item:
                        vids.append(item['contentDetails']['videoId'])
            if 'nextPageToken' in response:
                nextPageToken = response['nextPageToken']
            else:
                break
        return vids
    myvids = getplaylistvids('LM')
    playlistvid = getplaylistvids(playlistId)
    vids = set(myvids)-set(playlistvid)
    for vid in vids:
        try:
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": "",
                        "resourceId": {
                            "videoId": vid,
                            "kind": "youtube#video"
                        }
                    }
                }
            )
            response = request.execute()
            print(response)
            sleep(1)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
