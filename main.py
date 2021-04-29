# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from time import sleep
from contextlib import suppress

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
    client_secrets_file = "client_secret_678424978322-bbrt9776bau09pkrk2ktujb5gd2c77b6.apps.googleusercontent.com.json"
    destination_play_list = 'PLy907-qFs4c-xzTI-5KHGrNTiRdyWKRA3'
    source_play_list = 'LM'  # Replace if not using liked music
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes,redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    # credentials = flow.run_local_server()
    auth_url, _ = flow.authorization_url(prompt='consent')
    print(auth_url)
    code = input('Enter the authorization code: ')
    flow.fetch_token(code=code)
    credentials=flow.credentials
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

        if 'items' in response:
            items = response['items']
            for item in items:
                if "contentDetails" in item:
                    vids.append(item['contentDetails']['videoId'])
        while len(vids) < maxResults:
            sleep(1)
            if 'nextPageToken' in response:
                request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=pid,
                    maxResults=50,
                    pageToken= response['nextPageToken'],
                )
            else:
                request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=pid,
                    maxResults=50,
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

    source_vids = getplaylistvids(source_play_list)
    destination_vids = getplaylistvids(destination_play_list)
    vids = set(source_vids) - set(destination_vids)
    print(vids)
    for vid in vids:
        try:
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": destination_play_list,
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
