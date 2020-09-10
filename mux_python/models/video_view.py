# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class VideoView(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'view_total_upscaling': 'str',
        'preroll_ad_asset_hostname': 'str',
        'player_source_domain': 'str',
        'region': 'str',
        'viewer_user_agent': 'str',
        'preroll_requested': 'bool',
        'page_type': 'str',
        'startup_score': 'str',
        'view_seek_duration': 'int',
        'country_name': 'str',
        'player_source_height': 'int',
        'longitude': 'str',
        'buffering_count': 'int',
        'video_duration': 'int',
        'player_source_type': 'str',
        'city': 'str',
        'view_id': 'str',
        'platform_description': 'str',
        'video_startup_preroll_request_time': 'int',
        'viewer_device_name': 'str',
        'video_series': 'str',
        'viewer_application_name': 'str',
        'updated_at': 'str',
        'view_total_content_playback_time': 'int',
        'cdn': 'str',
        'player_instance_id': 'str',
        'video_language': 'str',
        'player_source_width': 'int',
        'player_error_message': 'str',
        'player_mux_plugin_version': 'str',
        'watched': 'bool',
        'playback_score': 'str',
        'page_url': 'str',
        'metro': 'str',
        'view_max_request_latency': 'int',
        'requests_for_first_preroll': 'int',
        'view_total_downscaling': 'str',
        'latitude': 'str',
        'player_source_host_name': 'str',
        'inserted_at': 'str',
        'view_end': 'str',
        'mux_embed_version': 'str',
        'player_language': 'str',
        'page_load_time': 'int',
        'viewer_device_category': 'str',
        'video_startup_preroll_load_time': 'int',
        'player_version': 'str',
        'watch_time': 'int',
        'player_source_stream_type': 'str',
        'preroll_ad_tag_hostname': 'str',
        'viewer_device_manufacturer': 'str',
        'rebuffering_score': 'str',
        'experiment_name': 'str',
        'viewer_os_version': 'str',
        'player_preload': 'bool',
        'buffering_duration': 'int',
        'player_view_count': 'int',
        'player_software': 'str',
        'player_load_time': 'int',
        'platform_summary': 'str',
        'video_encoding_variant': 'str',
        'player_width': 'int',
        'view_seek_count': 'int',
        'viewer_experience_score': 'str',
        'view_error_id': 'int',
        'video_variant_name': 'str',
        'preroll_played': 'bool',
        'viewer_application_engine': 'str',
        'viewer_os_architecture': 'str',
        'player_error_code': 'str',
        'buffering_rate': 'str',
        'events': 'list[VideoViewEvent]',
        'player_name': 'str',
        'view_start': 'str',
        'view_average_request_throughput': 'int',
        'video_producer': 'str',
        'error_type_id': 'int',
        'mux_viewer_id': 'str',
        'video_id': 'str',
        'continent_code': 'str',
        'session_id': 'str',
        'exit_before_video_start': 'bool',
        'video_content_type': 'str',
        'viewer_os_family': 'str',
        'player_poster': 'str',
        'view_average_request_latency': 'int',
        'video_variant_id': 'str',
        'player_source_duration': 'int',
        'player_source_url': 'str',
        'mux_api_version': 'str',
        'video_title': 'str',
        'id': 'str',
        'short_time': 'str',
        'rebuffer_percentage': 'str',
        'time_to_first_frame': 'int',
        'viewer_user_id': 'str',
        'video_stream_type': 'str',
        'player_startup_time': 'int',
        'viewer_application_version': 'str',
        'view_max_downscale_percentage': 'str',
        'view_max_upscale_percentage': 'str',
        'country_code': 'str',
        'used_fullscreen': 'bool',
        'isp': 'str',
        'property_id': 'int',
        'player_autoplay': 'bool',
        'player_height': 'int',
        'asn': 'int',
        'asn_name': 'str',
        'quality_score': 'str',
        'player_software_version': 'str',
        'player_mux_plugin_name': 'str'
    }

    attribute_map = {
        'view_total_upscaling': 'view_total_upscaling',
        'preroll_ad_asset_hostname': 'preroll_ad_asset_hostname',
        'player_source_domain': 'player_source_domain',
        'region': 'region',
        'viewer_user_agent': 'viewer_user_agent',
        'preroll_requested': 'preroll_requested',
        'page_type': 'page_type',
        'startup_score': 'startup_score',
        'view_seek_duration': 'view_seek_duration',
        'country_name': 'country_name',
        'player_source_height': 'player_source_height',
        'longitude': 'longitude',
        'buffering_count': 'buffering_count',
        'video_duration': 'video_duration',
        'player_source_type': 'player_source_type',
        'city': 'city',
        'view_id': 'view_id',
        'platform_description': 'platform_description',
        'video_startup_preroll_request_time': 'video_startup_preroll_request_time',
        'viewer_device_name': 'viewer_device_name',
        'video_series': 'video_series',
        'viewer_application_name': 'viewer_application_name',
        'updated_at': 'updated_at',
        'view_total_content_playback_time': 'view_total_content_playback_time',
        'cdn': 'cdn',
        'player_instance_id': 'player_instance_id',
        'video_language': 'video_language',
        'player_source_width': 'player_source_width',
        'player_error_message': 'player_error_message',
        'player_mux_plugin_version': 'player_mux_plugin_version',
        'watched': 'watched',
        'playback_score': 'playback_score',
        'page_url': 'page_url',
        'metro': 'metro',
        'view_max_request_latency': 'view_max_request_latency',
        'requests_for_first_preroll': 'requests_for_first_preroll',
        'view_total_downscaling': 'view_total_downscaling',
        'latitude': 'latitude',
        'player_source_host_name': 'player_source_host_name',
        'inserted_at': 'inserted_at',
        'view_end': 'view_end',
        'mux_embed_version': 'mux_embed_version',
        'player_language': 'player_language',
        'page_load_time': 'page_load_time',
        'viewer_device_category': 'viewer_device_category',
        'video_startup_preroll_load_time': 'video_startup_preroll_load_time',
        'player_version': 'player_version',
        'watch_time': 'watch_time',
        'player_source_stream_type': 'player_source_stream_type',
        'preroll_ad_tag_hostname': 'preroll_ad_tag_hostname',
        'viewer_device_manufacturer': 'viewer_device_manufacturer',
        'rebuffering_score': 'rebuffering_score',
        'experiment_name': 'experiment_name',
        'viewer_os_version': 'viewer_os_version',
        'player_preload': 'player_preload',
        'buffering_duration': 'buffering_duration',
        'player_view_count': 'player_view_count',
        'player_software': 'player_software',
        'player_load_time': 'player_load_time',
        'platform_summary': 'platform_summary',
        'video_encoding_variant': 'video_encoding_variant',
        'player_width': 'player_width',
        'view_seek_count': 'view_seek_count',
        'viewer_experience_score': 'viewer_experience_score',
        'view_error_id': 'view_error_id',
        'video_variant_name': 'video_variant_name',
        'preroll_played': 'preroll_played',
        'viewer_application_engine': 'viewer_application_engine',
        'viewer_os_architecture': 'viewer_os_architecture',
        'player_error_code': 'player_error_code',
        'buffering_rate': 'buffering_rate',
        'events': 'events',
        'player_name': 'player_name',
        'view_start': 'view_start',
        'view_average_request_throughput': 'view_average_request_throughput',
        'video_producer': 'video_producer',
        'error_type_id': 'error_type_id',
        'mux_viewer_id': 'mux_viewer_id',
        'video_id': 'video_id',
        'continent_code': 'continent_code',
        'session_id': 'session_id',
        'exit_before_video_start': 'exit_before_video_start',
        'video_content_type': 'video_content_type',
        'viewer_os_family': 'viewer_os_family',
        'player_poster': 'player_poster',
        'view_average_request_latency': 'view_average_request_latency',
        'video_variant_id': 'video_variant_id',
        'player_source_duration': 'player_source_duration',
        'player_source_url': 'player_source_url',
        'mux_api_version': 'mux_api_version',
        'video_title': 'video_title',
        'id': 'id',
        'short_time': 'short_time',
        'rebuffer_percentage': 'rebuffer_percentage',
        'time_to_first_frame': 'time_to_first_frame',
        'viewer_user_id': 'viewer_user_id',
        'video_stream_type': 'video_stream_type',
        'player_startup_time': 'player_startup_time',
        'viewer_application_version': 'viewer_application_version',
        'view_max_downscale_percentage': 'view_max_downscale_percentage',
        'view_max_upscale_percentage': 'view_max_upscale_percentage',
        'country_code': 'country_code',
        'used_fullscreen': 'used_fullscreen',
        'isp': 'isp',
        'property_id': 'property_id',
        'player_autoplay': 'player_autoplay',
        'player_height': 'player_height',
        'asn': 'asn',
        'asn_name': 'asn_name',
        'quality_score': 'quality_score',
        'player_software_version': 'player_software_version',
        'player_mux_plugin_name': 'player_mux_plugin_name'
    }

    def __init__(self, view_total_upscaling=None, preroll_ad_asset_hostname=None, player_source_domain=None, region=None, viewer_user_agent=None, preroll_requested=None, page_type=None, startup_score=None, view_seek_duration=None, country_name=None, player_source_height=None, longitude=None, buffering_count=None, video_duration=None, player_source_type=None, city=None, view_id=None, platform_description=None, video_startup_preroll_request_time=None, viewer_device_name=None, video_series=None, viewer_application_name=None, updated_at=None, view_total_content_playback_time=None, cdn=None, player_instance_id=None, video_language=None, player_source_width=None, player_error_message=None, player_mux_plugin_version=None, watched=None, playback_score=None, page_url=None, metro=None, view_max_request_latency=None, requests_for_first_preroll=None, view_total_downscaling=None, latitude=None, player_source_host_name=None, inserted_at=None, view_end=None, mux_embed_version=None, player_language=None, page_load_time=None, viewer_device_category=None, video_startup_preroll_load_time=None, player_version=None, watch_time=None, player_source_stream_type=None, preroll_ad_tag_hostname=None, viewer_device_manufacturer=None, rebuffering_score=None, experiment_name=None, viewer_os_version=None, player_preload=None, buffering_duration=None, player_view_count=None, player_software=None, player_load_time=None, platform_summary=None, video_encoding_variant=None, player_width=None, view_seek_count=None, viewer_experience_score=None, view_error_id=None, video_variant_name=None, preroll_played=None, viewer_application_engine=None, viewer_os_architecture=None, player_error_code=None, buffering_rate=None, events=None, player_name=None, view_start=None, view_average_request_throughput=None, video_producer=None, error_type_id=None, mux_viewer_id=None, video_id=None, continent_code=None, session_id=None, exit_before_video_start=None, video_content_type=None, viewer_os_family=None, player_poster=None, view_average_request_latency=None, video_variant_id=None, player_source_duration=None, player_source_url=None, mux_api_version=None, video_title=None, id=None, short_time=None, rebuffer_percentage=None, time_to_first_frame=None, viewer_user_id=None, video_stream_type=None, player_startup_time=None, viewer_application_version=None, view_max_downscale_percentage=None, view_max_upscale_percentage=None, country_code=None, used_fullscreen=None, isp=None, property_id=None, player_autoplay=None, player_height=None, asn=None, asn_name=None, quality_score=None, player_software_version=None, player_mux_plugin_name=None):  # noqa: E501
        """VideoView - a model defined in OpenAPI"""  # noqa: E501

        self._view_total_upscaling = None
        self._preroll_ad_asset_hostname = None
        self._player_source_domain = None
        self._region = None
        self._viewer_user_agent = None
        self._preroll_requested = None
        self._page_type = None
        self._startup_score = None
        self._view_seek_duration = None
        self._country_name = None
        self._player_source_height = None
        self._longitude = None
        self._buffering_count = None
        self._video_duration = None
        self._player_source_type = None
        self._city = None
        self._view_id = None
        self._platform_description = None
        self._video_startup_preroll_request_time = None
        self._viewer_device_name = None
        self._video_series = None
        self._viewer_application_name = None
        self._updated_at = None
        self._view_total_content_playback_time = None
        self._cdn = None
        self._player_instance_id = None
        self._video_language = None
        self._player_source_width = None
        self._player_error_message = None
        self._player_mux_plugin_version = None
        self._watched = None
        self._playback_score = None
        self._page_url = None
        self._metro = None
        self._view_max_request_latency = None
        self._requests_for_first_preroll = None
        self._view_total_downscaling = None
        self._latitude = None
        self._player_source_host_name = None
        self._inserted_at = None
        self._view_end = None
        self._mux_embed_version = None
        self._player_language = None
        self._page_load_time = None
        self._viewer_device_category = None
        self._video_startup_preroll_load_time = None
        self._player_version = None
        self._watch_time = None
        self._player_source_stream_type = None
        self._preroll_ad_tag_hostname = None
        self._viewer_device_manufacturer = None
        self._rebuffering_score = None
        self._experiment_name = None
        self._viewer_os_version = None
        self._player_preload = None
        self._buffering_duration = None
        self._player_view_count = None
        self._player_software = None
        self._player_load_time = None
        self._platform_summary = None
        self._video_encoding_variant = None
        self._player_width = None
        self._view_seek_count = None
        self._viewer_experience_score = None
        self._view_error_id = None
        self._video_variant_name = None
        self._preroll_played = None
        self._viewer_application_engine = None
        self._viewer_os_architecture = None
        self._player_error_code = None
        self._buffering_rate = None
        self._events = None
        self._player_name = None
        self._view_start = None
        self._view_average_request_throughput = None
        self._video_producer = None
        self._error_type_id = None
        self._mux_viewer_id = None
        self._video_id = None
        self._continent_code = None
        self._session_id = None
        self._exit_before_video_start = None
        self._video_content_type = None
        self._viewer_os_family = None
        self._player_poster = None
        self._view_average_request_latency = None
        self._video_variant_id = None
        self._player_source_duration = None
        self._player_source_url = None
        self._mux_api_version = None
        self._video_title = None
        self._id = None
        self._short_time = None
        self._rebuffer_percentage = None
        self._time_to_first_frame = None
        self._viewer_user_id = None
        self._video_stream_type = None
        self._player_startup_time = None
        self._viewer_application_version = None
        self._view_max_downscale_percentage = None
        self._view_max_upscale_percentage = None
        self._country_code = None
        self._used_fullscreen = None
        self._isp = None
        self._property_id = None
        self._player_autoplay = None
        self._player_height = None
        self._asn = None
        self._asn_name = None
        self._quality_score = None
        self._player_software_version = None
        self._player_mux_plugin_name = None
        self.discriminator = None

        if view_total_upscaling is not None:
            self.view_total_upscaling = view_total_upscaling
        if preroll_ad_asset_hostname is not None:
            self.preroll_ad_asset_hostname = preroll_ad_asset_hostname
        if player_source_domain is not None:
            self.player_source_domain = player_source_domain
        if region is not None:
            self.region = region
        if viewer_user_agent is not None:
            self.viewer_user_agent = viewer_user_agent
        if preroll_requested is not None:
            self.preroll_requested = preroll_requested
        if page_type is not None:
            self.page_type = page_type
        if startup_score is not None:
            self.startup_score = startup_score
        if view_seek_duration is not None:
            self.view_seek_duration = view_seek_duration
        if country_name is not None:
            self.country_name = country_name
        if player_source_height is not None:
            self.player_source_height = player_source_height
        if longitude is not None:
            self.longitude = longitude
        if buffering_count is not None:
            self.buffering_count = buffering_count
        if video_duration is not None:
            self.video_duration = video_duration
        if player_source_type is not None:
            self.player_source_type = player_source_type
        if city is not None:
            self.city = city
        if view_id is not None:
            self.view_id = view_id
        if platform_description is not None:
            self.platform_description = platform_description
        if video_startup_preroll_request_time is not None:
            self.video_startup_preroll_request_time = video_startup_preroll_request_time
        if viewer_device_name is not None:
            self.viewer_device_name = viewer_device_name
        if video_series is not None:
            self.video_series = video_series
        if viewer_application_name is not None:
            self.viewer_application_name = viewer_application_name
        if updated_at is not None:
            self.updated_at = updated_at
        if view_total_content_playback_time is not None:
            self.view_total_content_playback_time = view_total_content_playback_time
        if cdn is not None:
            self.cdn = cdn
        if player_instance_id is not None:
            self.player_instance_id = player_instance_id
        if video_language is not None:
            self.video_language = video_language
        if player_source_width is not None:
            self.player_source_width = player_source_width
        if player_error_message is not None:
            self.player_error_message = player_error_message
        if player_mux_plugin_version is not None:
            self.player_mux_plugin_version = player_mux_plugin_version
        if watched is not None:
            self.watched = watched
        if playback_score is not None:
            self.playback_score = playback_score
        if page_url is not None:
            self.page_url = page_url
        if metro is not None:
            self.metro = metro
        if view_max_request_latency is not None:
            self.view_max_request_latency = view_max_request_latency
        if requests_for_first_preroll is not None:
            self.requests_for_first_preroll = requests_for_first_preroll
        if view_total_downscaling is not None:
            self.view_total_downscaling = view_total_downscaling
        if latitude is not None:
            self.latitude = latitude
        if player_source_host_name is not None:
            self.player_source_host_name = player_source_host_name
        if inserted_at is not None:
            self.inserted_at = inserted_at
        if view_end is not None:
            self.view_end = view_end
        if mux_embed_version is not None:
            self.mux_embed_version = mux_embed_version
        if player_language is not None:
            self.player_language = player_language
        if page_load_time is not None:
            self.page_load_time = page_load_time
        if viewer_device_category is not None:
            self.viewer_device_category = viewer_device_category
        if video_startup_preroll_load_time is not None:
            self.video_startup_preroll_load_time = video_startup_preroll_load_time
        if player_version is not None:
            self.player_version = player_version
        if watch_time is not None:
            self.watch_time = watch_time
        if player_source_stream_type is not None:
            self.player_source_stream_type = player_source_stream_type
        if preroll_ad_tag_hostname is not None:
            self.preroll_ad_tag_hostname = preroll_ad_tag_hostname
        if viewer_device_manufacturer is not None:
            self.viewer_device_manufacturer = viewer_device_manufacturer
        if rebuffering_score is not None:
            self.rebuffering_score = rebuffering_score
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if viewer_os_version is not None:
            self.viewer_os_version = viewer_os_version
        if player_preload is not None:
            self.player_preload = player_preload
        if buffering_duration is not None:
            self.buffering_duration = buffering_duration
        if player_view_count is not None:
            self.player_view_count = player_view_count
        if player_software is not None:
            self.player_software = player_software
        if player_load_time is not None:
            self.player_load_time = player_load_time
        if platform_summary is not None:
            self.platform_summary = platform_summary
        if video_encoding_variant is not None:
            self.video_encoding_variant = video_encoding_variant
        if player_width is not None:
            self.player_width = player_width
        if view_seek_count is not None:
            self.view_seek_count = view_seek_count
        if viewer_experience_score is not None:
            self.viewer_experience_score = viewer_experience_score
        if view_error_id is not None:
            self.view_error_id = view_error_id
        if video_variant_name is not None:
            self.video_variant_name = video_variant_name
        if preroll_played is not None:
            self.preroll_played = preroll_played
        if viewer_application_engine is not None:
            self.viewer_application_engine = viewer_application_engine
        if viewer_os_architecture is not None:
            self.viewer_os_architecture = viewer_os_architecture
        if player_error_code is not None:
            self.player_error_code = player_error_code
        if buffering_rate is not None:
            self.buffering_rate = buffering_rate
        if events is not None:
            self.events = events
        if player_name is not None:
            self.player_name = player_name
        if view_start is not None:
            self.view_start = view_start
        if view_average_request_throughput is not None:
            self.view_average_request_throughput = view_average_request_throughput
        if video_producer is not None:
            self.video_producer = video_producer
        if error_type_id is not None:
            self.error_type_id = error_type_id
        if mux_viewer_id is not None:
            self.mux_viewer_id = mux_viewer_id
        if video_id is not None:
            self.video_id = video_id
        if continent_code is not None:
            self.continent_code = continent_code
        if session_id is not None:
            self.session_id = session_id
        if exit_before_video_start is not None:
            self.exit_before_video_start = exit_before_video_start
        if video_content_type is not None:
            self.video_content_type = video_content_type
        if viewer_os_family is not None:
            self.viewer_os_family = viewer_os_family
        if player_poster is not None:
            self.player_poster = player_poster
        if view_average_request_latency is not None:
            self.view_average_request_latency = view_average_request_latency
        if video_variant_id is not None:
            self.video_variant_id = video_variant_id
        if player_source_duration is not None:
            self.player_source_duration = player_source_duration
        if player_source_url is not None:
            self.player_source_url = player_source_url
        if mux_api_version is not None:
            self.mux_api_version = mux_api_version
        if video_title is not None:
            self.video_title = video_title
        if id is not None:
            self.id = id
        if short_time is not None:
            self.short_time = short_time
        if rebuffer_percentage is not None:
            self.rebuffer_percentage = rebuffer_percentage
        if time_to_first_frame is not None:
            self.time_to_first_frame = time_to_first_frame
        if viewer_user_id is not None:
            self.viewer_user_id = viewer_user_id
        if video_stream_type is not None:
            self.video_stream_type = video_stream_type
        if player_startup_time is not None:
            self.player_startup_time = player_startup_time
        if viewer_application_version is not None:
            self.viewer_application_version = viewer_application_version
        if view_max_downscale_percentage is not None:
            self.view_max_downscale_percentage = view_max_downscale_percentage
        if view_max_upscale_percentage is not None:
            self.view_max_upscale_percentage = view_max_upscale_percentage
        if country_code is not None:
            self.country_code = country_code
        if used_fullscreen is not None:
            self.used_fullscreen = used_fullscreen
        if isp is not None:
            self.isp = isp
        if property_id is not None:
            self.property_id = property_id
        if player_autoplay is not None:
            self.player_autoplay = player_autoplay
        if player_height is not None:
            self.player_height = player_height
        if asn is not None:
            self.asn = asn
        if asn_name is not None:
            self.asn_name = asn_name
        if quality_score is not None:
            self.quality_score = quality_score
        if player_software_version is not None:
            self.player_software_version = player_software_version
        if player_mux_plugin_name is not None:
            self.player_mux_plugin_name = player_mux_plugin_name

    @property
    def view_total_upscaling(self):
        """Gets the view_total_upscaling of this VideoView.  # noqa: E501


        :return: The view_total_upscaling of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_total_upscaling

    @view_total_upscaling.setter
    def view_total_upscaling(self, view_total_upscaling):
        """Sets the view_total_upscaling of this VideoView.


        :param view_total_upscaling: The view_total_upscaling of this VideoView.  # noqa: E501
        :type: str
        """

        self._view_total_upscaling = view_total_upscaling

    @property
    def preroll_ad_asset_hostname(self):
        """Gets the preroll_ad_asset_hostname of this VideoView.  # noqa: E501


        :return: The preroll_ad_asset_hostname of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._preroll_ad_asset_hostname

    @preroll_ad_asset_hostname.setter
    def preroll_ad_asset_hostname(self, preroll_ad_asset_hostname):
        """Sets the preroll_ad_asset_hostname of this VideoView.


        :param preroll_ad_asset_hostname: The preroll_ad_asset_hostname of this VideoView.  # noqa: E501
        :type: str
        """

        self._preroll_ad_asset_hostname = preroll_ad_asset_hostname

    @property
    def player_source_domain(self):
        """Gets the player_source_domain of this VideoView.  # noqa: E501


        :return: The player_source_domain of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_source_domain

    @player_source_domain.setter
    def player_source_domain(self, player_source_domain):
        """Sets the player_source_domain of this VideoView.


        :param player_source_domain: The player_source_domain of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_source_domain = player_source_domain

    @property
    def region(self):
        """Gets the region of this VideoView.  # noqa: E501


        :return: The region of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this VideoView.


        :param region: The region of this VideoView.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def viewer_user_agent(self):
        """Gets the viewer_user_agent of this VideoView.  # noqa: E501


        :return: The viewer_user_agent of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_user_agent

    @viewer_user_agent.setter
    def viewer_user_agent(self, viewer_user_agent):
        """Sets the viewer_user_agent of this VideoView.


        :param viewer_user_agent: The viewer_user_agent of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_user_agent = viewer_user_agent

    @property
    def preroll_requested(self):
        """Gets the preroll_requested of this VideoView.  # noqa: E501


        :return: The preroll_requested of this VideoView.  # noqa: E501
        :rtype: bool
        """
        return self._preroll_requested

    @preroll_requested.setter
    def preroll_requested(self, preroll_requested):
        """Sets the preroll_requested of this VideoView.


        :param preroll_requested: The preroll_requested of this VideoView.  # noqa: E501
        :type: bool
        """

        self._preroll_requested = preroll_requested

    @property
    def page_type(self):
        """Gets the page_type of this VideoView.  # noqa: E501


        :return: The page_type of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._page_type

    @page_type.setter
    def page_type(self, page_type):
        """Sets the page_type of this VideoView.


        :param page_type: The page_type of this VideoView.  # noqa: E501
        :type: str
        """

        self._page_type = page_type

    @property
    def startup_score(self):
        """Gets the startup_score of this VideoView.  # noqa: E501


        :return: The startup_score of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._startup_score

    @startup_score.setter
    def startup_score(self, startup_score):
        """Sets the startup_score of this VideoView.


        :param startup_score: The startup_score of this VideoView.  # noqa: E501
        :type: str
        """

        self._startup_score = startup_score

    @property
    def view_seek_duration(self):
        """Gets the view_seek_duration of this VideoView.  # noqa: E501


        :return: The view_seek_duration of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._view_seek_duration

    @view_seek_duration.setter
    def view_seek_duration(self, view_seek_duration):
        """Sets the view_seek_duration of this VideoView.


        :param view_seek_duration: The view_seek_duration of this VideoView.  # noqa: E501
        :type: int
        """

        self._view_seek_duration = view_seek_duration

    @property
    def country_name(self):
        """Gets the country_name of this VideoView.  # noqa: E501


        :return: The country_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this VideoView.


        :param country_name: The country_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def player_source_height(self):
        """Gets the player_source_height of this VideoView.  # noqa: E501


        :return: The player_source_height of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_source_height

    @player_source_height.setter
    def player_source_height(self, player_source_height):
        """Sets the player_source_height of this VideoView.


        :param player_source_height: The player_source_height of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_source_height = player_source_height

    @property
    def longitude(self):
        """Gets the longitude of this VideoView.  # noqa: E501


        :return: The longitude of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this VideoView.


        :param longitude: The longitude of this VideoView.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

    @property
    def buffering_count(self):
        """Gets the buffering_count of this VideoView.  # noqa: E501


        :return: The buffering_count of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._buffering_count

    @buffering_count.setter
    def buffering_count(self, buffering_count):
        """Sets the buffering_count of this VideoView.


        :param buffering_count: The buffering_count of this VideoView.  # noqa: E501
        :type: int
        """

        self._buffering_count = buffering_count

    @property
    def video_duration(self):
        """Gets the video_duration of this VideoView.  # noqa: E501


        :return: The video_duration of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._video_duration

    @video_duration.setter
    def video_duration(self, video_duration):
        """Sets the video_duration of this VideoView.


        :param video_duration: The video_duration of this VideoView.  # noqa: E501
        :type: int
        """

        self._video_duration = video_duration

    @property
    def player_source_type(self):
        """Gets the player_source_type of this VideoView.  # noqa: E501


        :return: The player_source_type of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_source_type

    @player_source_type.setter
    def player_source_type(self, player_source_type):
        """Sets the player_source_type of this VideoView.


        :param player_source_type: The player_source_type of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_source_type = player_source_type

    @property
    def city(self):
        """Gets the city of this VideoView.  # noqa: E501


        :return: The city of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this VideoView.


        :param city: The city of this VideoView.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def view_id(self):
        """Gets the view_id of this VideoView.  # noqa: E501


        :return: The view_id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """Sets the view_id of this VideoView.


        :param view_id: The view_id of this VideoView.  # noqa: E501
        :type: str
        """

        self._view_id = view_id

    @property
    def platform_description(self):
        """Gets the platform_description of this VideoView.  # noqa: E501


        :return: The platform_description of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._platform_description

    @platform_description.setter
    def platform_description(self, platform_description):
        """Sets the platform_description of this VideoView.


        :param platform_description: The platform_description of this VideoView.  # noqa: E501
        :type: str
        """

        self._platform_description = platform_description

    @property
    def video_startup_preroll_request_time(self):
        """Gets the video_startup_preroll_request_time of this VideoView.  # noqa: E501


        :return: The video_startup_preroll_request_time of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._video_startup_preroll_request_time

    @video_startup_preroll_request_time.setter
    def video_startup_preroll_request_time(self, video_startup_preroll_request_time):
        """Sets the video_startup_preroll_request_time of this VideoView.


        :param video_startup_preroll_request_time: The video_startup_preroll_request_time of this VideoView.  # noqa: E501
        :type: int
        """

        self._video_startup_preroll_request_time = video_startup_preroll_request_time

    @property
    def viewer_device_name(self):
        """Gets the viewer_device_name of this VideoView.  # noqa: E501


        :return: The viewer_device_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_device_name

    @viewer_device_name.setter
    def viewer_device_name(self, viewer_device_name):
        """Sets the viewer_device_name of this VideoView.


        :param viewer_device_name: The viewer_device_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_device_name = viewer_device_name

    @property
    def video_series(self):
        """Gets the video_series of this VideoView.  # noqa: E501


        :return: The video_series of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_series

    @video_series.setter
    def video_series(self, video_series):
        """Sets the video_series of this VideoView.


        :param video_series: The video_series of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_series = video_series

    @property
    def viewer_application_name(self):
        """Gets the viewer_application_name of this VideoView.  # noqa: E501


        :return: The viewer_application_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_application_name

    @viewer_application_name.setter
    def viewer_application_name(self, viewer_application_name):
        """Sets the viewer_application_name of this VideoView.


        :param viewer_application_name: The viewer_application_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_application_name = viewer_application_name

    @property
    def updated_at(self):
        """Gets the updated_at of this VideoView.  # noqa: E501


        :return: The updated_at of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VideoView.


        :param updated_at: The updated_at of this VideoView.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def view_total_content_playback_time(self):
        """Gets the view_total_content_playback_time of this VideoView.  # noqa: E501


        :return: The view_total_content_playback_time of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._view_total_content_playback_time

    @view_total_content_playback_time.setter
    def view_total_content_playback_time(self, view_total_content_playback_time):
        """Sets the view_total_content_playback_time of this VideoView.


        :param view_total_content_playback_time: The view_total_content_playback_time of this VideoView.  # noqa: E501
        :type: int
        """

        self._view_total_content_playback_time = view_total_content_playback_time

    @property
    def cdn(self):
        """Gets the cdn of this VideoView.  # noqa: E501


        :return: The cdn of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._cdn

    @cdn.setter
    def cdn(self, cdn):
        """Sets the cdn of this VideoView.


        :param cdn: The cdn of this VideoView.  # noqa: E501
        :type: str
        """

        self._cdn = cdn

    @property
    def player_instance_id(self):
        """Gets the player_instance_id of this VideoView.  # noqa: E501


        :return: The player_instance_id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_instance_id

    @player_instance_id.setter
    def player_instance_id(self, player_instance_id):
        """Sets the player_instance_id of this VideoView.


        :param player_instance_id: The player_instance_id of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_instance_id = player_instance_id

    @property
    def video_language(self):
        """Gets the video_language of this VideoView.  # noqa: E501


        :return: The video_language of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_language

    @video_language.setter
    def video_language(self, video_language):
        """Sets the video_language of this VideoView.


        :param video_language: The video_language of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_language = video_language

    @property
    def player_source_width(self):
        """Gets the player_source_width of this VideoView.  # noqa: E501


        :return: The player_source_width of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_source_width

    @player_source_width.setter
    def player_source_width(self, player_source_width):
        """Sets the player_source_width of this VideoView.


        :param player_source_width: The player_source_width of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_source_width = player_source_width

    @property
    def player_error_message(self):
        """Gets the player_error_message of this VideoView.  # noqa: E501


        :return: The player_error_message of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_error_message

    @player_error_message.setter
    def player_error_message(self, player_error_message):
        """Sets the player_error_message of this VideoView.


        :param player_error_message: The player_error_message of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_error_message = player_error_message

    @property
    def player_mux_plugin_version(self):
        """Gets the player_mux_plugin_version of this VideoView.  # noqa: E501


        :return: The player_mux_plugin_version of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_mux_plugin_version

    @player_mux_plugin_version.setter
    def player_mux_plugin_version(self, player_mux_plugin_version):
        """Sets the player_mux_plugin_version of this VideoView.


        :param player_mux_plugin_version: The player_mux_plugin_version of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_mux_plugin_version = player_mux_plugin_version

    @property
    def watched(self):
        """Gets the watched of this VideoView.  # noqa: E501


        :return: The watched of this VideoView.  # noqa: E501
        :rtype: bool
        """
        return self._watched

    @watched.setter
    def watched(self, watched):
        """Sets the watched of this VideoView.


        :param watched: The watched of this VideoView.  # noqa: E501
        :type: bool
        """

        self._watched = watched

    @property
    def playback_score(self):
        """Gets the playback_score of this VideoView.  # noqa: E501


        :return: The playback_score of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._playback_score

    @playback_score.setter
    def playback_score(self, playback_score):
        """Sets the playback_score of this VideoView.


        :param playback_score: The playback_score of this VideoView.  # noqa: E501
        :type: str
        """

        self._playback_score = playback_score

    @property
    def page_url(self):
        """Gets the page_url of this VideoView.  # noqa: E501


        :return: The page_url of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._page_url

    @page_url.setter
    def page_url(self, page_url):
        """Sets the page_url of this VideoView.


        :param page_url: The page_url of this VideoView.  # noqa: E501
        :type: str
        """

        self._page_url = page_url

    @property
    def metro(self):
        """Gets the metro of this VideoView.  # noqa: E501


        :return: The metro of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this VideoView.


        :param metro: The metro of this VideoView.  # noqa: E501
        :type: str
        """

        self._metro = metro

    @property
    def view_max_request_latency(self):
        """Gets the view_max_request_latency of this VideoView.  # noqa: E501


        :return: The view_max_request_latency of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._view_max_request_latency

    @view_max_request_latency.setter
    def view_max_request_latency(self, view_max_request_latency):
        """Sets the view_max_request_latency of this VideoView.


        :param view_max_request_latency: The view_max_request_latency of this VideoView.  # noqa: E501
        :type: int
        """

        self._view_max_request_latency = view_max_request_latency

    @property
    def requests_for_first_preroll(self):
        """Gets the requests_for_first_preroll of this VideoView.  # noqa: E501


        :return: The requests_for_first_preroll of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._requests_for_first_preroll

    @requests_for_first_preroll.setter
    def requests_for_first_preroll(self, requests_for_first_preroll):
        """Sets the requests_for_first_preroll of this VideoView.


        :param requests_for_first_preroll: The requests_for_first_preroll of this VideoView.  # noqa: E501
        :type: int
        """

        self._requests_for_first_preroll = requests_for_first_preroll

    @property
    def view_total_downscaling(self):
        """Gets the view_total_downscaling of this VideoView.  # noqa: E501


        :return: The view_total_downscaling of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_total_downscaling

    @view_total_downscaling.setter
    def view_total_downscaling(self, view_total_downscaling):
        """Sets the view_total_downscaling of this VideoView.


        :param view_total_downscaling: The view_total_downscaling of this VideoView.  # noqa: E501
        :type: str
        """

        self._view_total_downscaling = view_total_downscaling

    @property
    def latitude(self):
        """Gets the latitude of this VideoView.  # noqa: E501


        :return: The latitude of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this VideoView.


        :param latitude: The latitude of this VideoView.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def player_source_host_name(self):
        """Gets the player_source_host_name of this VideoView.  # noqa: E501


        :return: The player_source_host_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_source_host_name

    @player_source_host_name.setter
    def player_source_host_name(self, player_source_host_name):
        """Sets the player_source_host_name of this VideoView.


        :param player_source_host_name: The player_source_host_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_source_host_name = player_source_host_name

    @property
    def inserted_at(self):
        """Gets the inserted_at of this VideoView.  # noqa: E501


        :return: The inserted_at of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._inserted_at

    @inserted_at.setter
    def inserted_at(self, inserted_at):
        """Sets the inserted_at of this VideoView.


        :param inserted_at: The inserted_at of this VideoView.  # noqa: E501
        :type: str
        """

        self._inserted_at = inserted_at

    @property
    def view_end(self):
        """Gets the view_end of this VideoView.  # noqa: E501


        :return: The view_end of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_end

    @view_end.setter
    def view_end(self, view_end):
        """Sets the view_end of this VideoView.


        :param view_end: The view_end of this VideoView.  # noqa: E501
        :type: str
        """

        self._view_end = view_end

    @property
    def mux_embed_version(self):
        """Gets the mux_embed_version of this VideoView.  # noqa: E501


        :return: The mux_embed_version of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._mux_embed_version

    @mux_embed_version.setter
    def mux_embed_version(self, mux_embed_version):
        """Sets the mux_embed_version of this VideoView.


        :param mux_embed_version: The mux_embed_version of this VideoView.  # noqa: E501
        :type: str
        """

        self._mux_embed_version = mux_embed_version

    @property
    def player_language(self):
        """Gets the player_language of this VideoView.  # noqa: E501


        :return: The player_language of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_language

    @player_language.setter
    def player_language(self, player_language):
        """Sets the player_language of this VideoView.


        :param player_language: The player_language of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_language = player_language

    @property
    def page_load_time(self):
        """Gets the page_load_time of this VideoView.  # noqa: E501


        :return: The page_load_time of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._page_load_time

    @page_load_time.setter
    def page_load_time(self, page_load_time):
        """Sets the page_load_time of this VideoView.


        :param page_load_time: The page_load_time of this VideoView.  # noqa: E501
        :type: int
        """

        self._page_load_time = page_load_time

    @property
    def viewer_device_category(self):
        """Gets the viewer_device_category of this VideoView.  # noqa: E501


        :return: The viewer_device_category of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_device_category

    @viewer_device_category.setter
    def viewer_device_category(self, viewer_device_category):
        """Sets the viewer_device_category of this VideoView.


        :param viewer_device_category: The viewer_device_category of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_device_category = viewer_device_category

    @property
    def video_startup_preroll_load_time(self):
        """Gets the video_startup_preroll_load_time of this VideoView.  # noqa: E501


        :return: The video_startup_preroll_load_time of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._video_startup_preroll_load_time

    @video_startup_preroll_load_time.setter
    def video_startup_preroll_load_time(self, video_startup_preroll_load_time):
        """Sets the video_startup_preroll_load_time of this VideoView.


        :param video_startup_preroll_load_time: The video_startup_preroll_load_time of this VideoView.  # noqa: E501
        :type: int
        """

        self._video_startup_preroll_load_time = video_startup_preroll_load_time

    @property
    def player_version(self):
        """Gets the player_version of this VideoView.  # noqa: E501


        :return: The player_version of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_version

    @player_version.setter
    def player_version(self, player_version):
        """Sets the player_version of this VideoView.


        :param player_version: The player_version of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_version = player_version

    @property
    def watch_time(self):
        """Gets the watch_time of this VideoView.  # noqa: E501


        :return: The watch_time of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._watch_time

    @watch_time.setter
    def watch_time(self, watch_time):
        """Sets the watch_time of this VideoView.


        :param watch_time: The watch_time of this VideoView.  # noqa: E501
        :type: int
        """

        self._watch_time = watch_time

    @property
    def player_source_stream_type(self):
        """Gets the player_source_stream_type of this VideoView.  # noqa: E501


        :return: The player_source_stream_type of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_source_stream_type

    @player_source_stream_type.setter
    def player_source_stream_type(self, player_source_stream_type):
        """Sets the player_source_stream_type of this VideoView.


        :param player_source_stream_type: The player_source_stream_type of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_source_stream_type = player_source_stream_type

    @property
    def preroll_ad_tag_hostname(self):
        """Gets the preroll_ad_tag_hostname of this VideoView.  # noqa: E501


        :return: The preroll_ad_tag_hostname of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._preroll_ad_tag_hostname

    @preroll_ad_tag_hostname.setter
    def preroll_ad_tag_hostname(self, preroll_ad_tag_hostname):
        """Sets the preroll_ad_tag_hostname of this VideoView.


        :param preroll_ad_tag_hostname: The preroll_ad_tag_hostname of this VideoView.  # noqa: E501
        :type: str
        """

        self._preroll_ad_tag_hostname = preroll_ad_tag_hostname

    @property
    def viewer_device_manufacturer(self):
        """Gets the viewer_device_manufacturer of this VideoView.  # noqa: E501


        :return: The viewer_device_manufacturer of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_device_manufacturer

    @viewer_device_manufacturer.setter
    def viewer_device_manufacturer(self, viewer_device_manufacturer):
        """Sets the viewer_device_manufacturer of this VideoView.


        :param viewer_device_manufacturer: The viewer_device_manufacturer of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_device_manufacturer = viewer_device_manufacturer

    @property
    def rebuffering_score(self):
        """Gets the rebuffering_score of this VideoView.  # noqa: E501


        :return: The rebuffering_score of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._rebuffering_score

    @rebuffering_score.setter
    def rebuffering_score(self, rebuffering_score):
        """Sets the rebuffering_score of this VideoView.


        :param rebuffering_score: The rebuffering_score of this VideoView.  # noqa: E501
        :type: str
        """

        self._rebuffering_score = rebuffering_score

    @property
    def experiment_name(self):
        """Gets the experiment_name of this VideoView.  # noqa: E501


        :return: The experiment_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this VideoView.


        :param experiment_name: The experiment_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._experiment_name = experiment_name

    @property
    def viewer_os_version(self):
        """Gets the viewer_os_version of this VideoView.  # noqa: E501


        :return: The viewer_os_version of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_os_version

    @viewer_os_version.setter
    def viewer_os_version(self, viewer_os_version):
        """Sets the viewer_os_version of this VideoView.


        :param viewer_os_version: The viewer_os_version of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_os_version = viewer_os_version

    @property
    def player_preload(self):
        """Gets the player_preload of this VideoView.  # noqa: E501


        :return: The player_preload of this VideoView.  # noqa: E501
        :rtype: bool
        """
        return self._player_preload

    @player_preload.setter
    def player_preload(self, player_preload):
        """Sets the player_preload of this VideoView.


        :param player_preload: The player_preload of this VideoView.  # noqa: E501
        :type: bool
        """

        self._player_preload = player_preload

    @property
    def buffering_duration(self):
        """Gets the buffering_duration of this VideoView.  # noqa: E501


        :return: The buffering_duration of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._buffering_duration

    @buffering_duration.setter
    def buffering_duration(self, buffering_duration):
        """Sets the buffering_duration of this VideoView.


        :param buffering_duration: The buffering_duration of this VideoView.  # noqa: E501
        :type: int
        """

        self._buffering_duration = buffering_duration

    @property
    def player_view_count(self):
        """Gets the player_view_count of this VideoView.  # noqa: E501


        :return: The player_view_count of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_view_count

    @player_view_count.setter
    def player_view_count(self, player_view_count):
        """Sets the player_view_count of this VideoView.


        :param player_view_count: The player_view_count of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_view_count = player_view_count

    @property
    def player_software(self):
        """Gets the player_software of this VideoView.  # noqa: E501


        :return: The player_software of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_software

    @player_software.setter
    def player_software(self, player_software):
        """Sets the player_software of this VideoView.


        :param player_software: The player_software of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_software = player_software

    @property
    def player_load_time(self):
        """Gets the player_load_time of this VideoView.  # noqa: E501


        :return: The player_load_time of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_load_time

    @player_load_time.setter
    def player_load_time(self, player_load_time):
        """Sets the player_load_time of this VideoView.


        :param player_load_time: The player_load_time of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_load_time = player_load_time

    @property
    def platform_summary(self):
        """Gets the platform_summary of this VideoView.  # noqa: E501


        :return: The platform_summary of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._platform_summary

    @platform_summary.setter
    def platform_summary(self, platform_summary):
        """Sets the platform_summary of this VideoView.


        :param platform_summary: The platform_summary of this VideoView.  # noqa: E501
        :type: str
        """

        self._platform_summary = platform_summary

    @property
    def video_encoding_variant(self):
        """Gets the video_encoding_variant of this VideoView.  # noqa: E501


        :return: The video_encoding_variant of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_encoding_variant

    @video_encoding_variant.setter
    def video_encoding_variant(self, video_encoding_variant):
        """Sets the video_encoding_variant of this VideoView.


        :param video_encoding_variant: The video_encoding_variant of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_encoding_variant = video_encoding_variant

    @property
    def player_width(self):
        """Gets the player_width of this VideoView.  # noqa: E501


        :return: The player_width of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_width

    @player_width.setter
    def player_width(self, player_width):
        """Sets the player_width of this VideoView.


        :param player_width: The player_width of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_width = player_width

    @property
    def view_seek_count(self):
        """Gets the view_seek_count of this VideoView.  # noqa: E501


        :return: The view_seek_count of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._view_seek_count

    @view_seek_count.setter
    def view_seek_count(self, view_seek_count):
        """Sets the view_seek_count of this VideoView.


        :param view_seek_count: The view_seek_count of this VideoView.  # noqa: E501
        :type: int
        """

        self._view_seek_count = view_seek_count

    @property
    def viewer_experience_score(self):
        """Gets the viewer_experience_score of this VideoView.  # noqa: E501


        :return: The viewer_experience_score of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_experience_score

    @viewer_experience_score.setter
    def viewer_experience_score(self, viewer_experience_score):
        """Sets the viewer_experience_score of this VideoView.


        :param viewer_experience_score: The viewer_experience_score of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_experience_score = viewer_experience_score

    @property
    def view_error_id(self):
        """Gets the view_error_id of this VideoView.  # noqa: E501


        :return: The view_error_id of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._view_error_id

    @view_error_id.setter
    def view_error_id(self, view_error_id):
        """Sets the view_error_id of this VideoView.


        :param view_error_id: The view_error_id of this VideoView.  # noqa: E501
        :type: int
        """

        self._view_error_id = view_error_id

    @property
    def video_variant_name(self):
        """Gets the video_variant_name of this VideoView.  # noqa: E501


        :return: The video_variant_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_variant_name

    @video_variant_name.setter
    def video_variant_name(self, video_variant_name):
        """Sets the video_variant_name of this VideoView.


        :param video_variant_name: The video_variant_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_variant_name = video_variant_name

    @property
    def preroll_played(self):
        """Gets the preroll_played of this VideoView.  # noqa: E501


        :return: The preroll_played of this VideoView.  # noqa: E501
        :rtype: bool
        """
        return self._preroll_played

    @preroll_played.setter
    def preroll_played(self, preroll_played):
        """Sets the preroll_played of this VideoView.


        :param preroll_played: The preroll_played of this VideoView.  # noqa: E501
        :type: bool
        """

        self._preroll_played = preroll_played

    @property
    def viewer_application_engine(self):
        """Gets the viewer_application_engine of this VideoView.  # noqa: E501


        :return: The viewer_application_engine of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_application_engine

    @viewer_application_engine.setter
    def viewer_application_engine(self, viewer_application_engine):
        """Sets the viewer_application_engine of this VideoView.


        :param viewer_application_engine: The viewer_application_engine of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_application_engine = viewer_application_engine

    @property
    def viewer_os_architecture(self):
        """Gets the viewer_os_architecture of this VideoView.  # noqa: E501


        :return: The viewer_os_architecture of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_os_architecture

    @viewer_os_architecture.setter
    def viewer_os_architecture(self, viewer_os_architecture):
        """Sets the viewer_os_architecture of this VideoView.


        :param viewer_os_architecture: The viewer_os_architecture of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_os_architecture = viewer_os_architecture

    @property
    def player_error_code(self):
        """Gets the player_error_code of this VideoView.  # noqa: E501


        :return: The player_error_code of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_error_code

    @player_error_code.setter
    def player_error_code(self, player_error_code):
        """Sets the player_error_code of this VideoView.


        :param player_error_code: The player_error_code of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_error_code = player_error_code

    @property
    def buffering_rate(self):
        """Gets the buffering_rate of this VideoView.  # noqa: E501


        :return: The buffering_rate of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._buffering_rate

    @buffering_rate.setter
    def buffering_rate(self, buffering_rate):
        """Sets the buffering_rate of this VideoView.


        :param buffering_rate: The buffering_rate of this VideoView.  # noqa: E501
        :type: str
        """

        self._buffering_rate = buffering_rate

    @property
    def events(self):
        """Gets the events of this VideoView.  # noqa: E501


        :return: The events of this VideoView.  # noqa: E501
        :rtype: list[VideoViewEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this VideoView.


        :param events: The events of this VideoView.  # noqa: E501
        :type: list[VideoViewEvent]
        """

        self._events = events

    @property
    def player_name(self):
        """Gets the player_name of this VideoView.  # noqa: E501


        :return: The player_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_name

    @player_name.setter
    def player_name(self, player_name):
        """Sets the player_name of this VideoView.


        :param player_name: The player_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_name = player_name

    @property
    def view_start(self):
        """Gets the view_start of this VideoView.  # noqa: E501


        :return: The view_start of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_start

    @view_start.setter
    def view_start(self, view_start):
        """Sets the view_start of this VideoView.


        :param view_start: The view_start of this VideoView.  # noqa: E501
        :type: str
        """

        self._view_start = view_start

    @property
    def view_average_request_throughput(self):
        """Gets the view_average_request_throughput of this VideoView.  # noqa: E501


        :return: The view_average_request_throughput of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._view_average_request_throughput

    @view_average_request_throughput.setter
    def view_average_request_throughput(self, view_average_request_throughput):
        """Sets the view_average_request_throughput of this VideoView.


        :param view_average_request_throughput: The view_average_request_throughput of this VideoView.  # noqa: E501
        :type: int
        """

        self._view_average_request_throughput = view_average_request_throughput

    @property
    def video_producer(self):
        """Gets the video_producer of this VideoView.  # noqa: E501


        :return: The video_producer of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_producer

    @video_producer.setter
    def video_producer(self, video_producer):
        """Sets the video_producer of this VideoView.


        :param video_producer: The video_producer of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_producer = video_producer

    @property
    def error_type_id(self):
        """Gets the error_type_id of this VideoView.  # noqa: E501


        :return: The error_type_id of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._error_type_id

    @error_type_id.setter
    def error_type_id(self, error_type_id):
        """Sets the error_type_id of this VideoView.


        :param error_type_id: The error_type_id of this VideoView.  # noqa: E501
        :type: int
        """

        self._error_type_id = error_type_id

    @property
    def mux_viewer_id(self):
        """Gets the mux_viewer_id of this VideoView.  # noqa: E501


        :return: The mux_viewer_id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._mux_viewer_id

    @mux_viewer_id.setter
    def mux_viewer_id(self, mux_viewer_id):
        """Sets the mux_viewer_id of this VideoView.


        :param mux_viewer_id: The mux_viewer_id of this VideoView.  # noqa: E501
        :type: str
        """

        self._mux_viewer_id = mux_viewer_id

    @property
    def video_id(self):
        """Gets the video_id of this VideoView.  # noqa: E501


        :return: The video_id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this VideoView.


        :param video_id: The video_id of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_id = video_id

    @property
    def continent_code(self):
        """Gets the continent_code of this VideoView.  # noqa: E501


        :return: The continent_code of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._continent_code

    @continent_code.setter
    def continent_code(self, continent_code):
        """Sets the continent_code of this VideoView.


        :param continent_code: The continent_code of this VideoView.  # noqa: E501
        :type: str
        """

        self._continent_code = continent_code

    @property
    def session_id(self):
        """Gets the session_id of this VideoView.  # noqa: E501


        :return: The session_id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this VideoView.


        :param session_id: The session_id of this VideoView.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def exit_before_video_start(self):
        """Gets the exit_before_video_start of this VideoView.  # noqa: E501


        :return: The exit_before_video_start of this VideoView.  # noqa: E501
        :rtype: bool
        """
        return self._exit_before_video_start

    @exit_before_video_start.setter
    def exit_before_video_start(self, exit_before_video_start):
        """Sets the exit_before_video_start of this VideoView.


        :param exit_before_video_start: The exit_before_video_start of this VideoView.  # noqa: E501
        :type: bool
        """

        self._exit_before_video_start = exit_before_video_start

    @property
    def video_content_type(self):
        """Gets the video_content_type of this VideoView.  # noqa: E501


        :return: The video_content_type of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_content_type

    @video_content_type.setter
    def video_content_type(self, video_content_type):
        """Sets the video_content_type of this VideoView.


        :param video_content_type: The video_content_type of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_content_type = video_content_type

    @property
    def viewer_os_family(self):
        """Gets the viewer_os_family of this VideoView.  # noqa: E501


        :return: The viewer_os_family of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_os_family

    @viewer_os_family.setter
    def viewer_os_family(self, viewer_os_family):
        """Sets the viewer_os_family of this VideoView.


        :param viewer_os_family: The viewer_os_family of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_os_family = viewer_os_family

    @property
    def player_poster(self):
        """Gets the player_poster of this VideoView.  # noqa: E501


        :return: The player_poster of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_poster

    @player_poster.setter
    def player_poster(self, player_poster):
        """Sets the player_poster of this VideoView.


        :param player_poster: The player_poster of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_poster = player_poster

    @property
    def view_average_request_latency(self):
        """Gets the view_average_request_latency of this VideoView.  # noqa: E501


        :return: The view_average_request_latency of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._view_average_request_latency

    @view_average_request_latency.setter
    def view_average_request_latency(self, view_average_request_latency):
        """Sets the view_average_request_latency of this VideoView.


        :param view_average_request_latency: The view_average_request_latency of this VideoView.  # noqa: E501
        :type: int
        """

        self._view_average_request_latency = view_average_request_latency

    @property
    def video_variant_id(self):
        """Gets the video_variant_id of this VideoView.  # noqa: E501


        :return: The video_variant_id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_variant_id

    @video_variant_id.setter
    def video_variant_id(self, video_variant_id):
        """Sets the video_variant_id of this VideoView.


        :param video_variant_id: The video_variant_id of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_variant_id = video_variant_id

    @property
    def player_source_duration(self):
        """Gets the player_source_duration of this VideoView.  # noqa: E501


        :return: The player_source_duration of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_source_duration

    @player_source_duration.setter
    def player_source_duration(self, player_source_duration):
        """Sets the player_source_duration of this VideoView.


        :param player_source_duration: The player_source_duration of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_source_duration = player_source_duration

    @property
    def player_source_url(self):
        """Gets the player_source_url of this VideoView.  # noqa: E501


        :return: The player_source_url of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_source_url

    @player_source_url.setter
    def player_source_url(self, player_source_url):
        """Sets the player_source_url of this VideoView.


        :param player_source_url: The player_source_url of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_source_url = player_source_url

    @property
    def mux_api_version(self):
        """Gets the mux_api_version of this VideoView.  # noqa: E501


        :return: The mux_api_version of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._mux_api_version

    @mux_api_version.setter
    def mux_api_version(self, mux_api_version):
        """Sets the mux_api_version of this VideoView.


        :param mux_api_version: The mux_api_version of this VideoView.  # noqa: E501
        :type: str
        """

        self._mux_api_version = mux_api_version

    @property
    def video_title(self):
        """Gets the video_title of this VideoView.  # noqa: E501


        :return: The video_title of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_title

    @video_title.setter
    def video_title(self, video_title):
        """Sets the video_title of this VideoView.


        :param video_title: The video_title of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_title = video_title

    @property
    def id(self):
        """Gets the id of this VideoView.  # noqa: E501


        :return: The id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VideoView.


        :param id: The id of this VideoView.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def short_time(self):
        """Gets the short_time of this VideoView.  # noqa: E501


        :return: The short_time of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._short_time

    @short_time.setter
    def short_time(self, short_time):
        """Sets the short_time of this VideoView.


        :param short_time: The short_time of this VideoView.  # noqa: E501
        :type: str
        """

        self._short_time = short_time

    @property
    def rebuffer_percentage(self):
        """Gets the rebuffer_percentage of this VideoView.  # noqa: E501


        :return: The rebuffer_percentage of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._rebuffer_percentage

    @rebuffer_percentage.setter
    def rebuffer_percentage(self, rebuffer_percentage):
        """Sets the rebuffer_percentage of this VideoView.


        :param rebuffer_percentage: The rebuffer_percentage of this VideoView.  # noqa: E501
        :type: str
        """

        self._rebuffer_percentage = rebuffer_percentage

    @property
    def time_to_first_frame(self):
        """Gets the time_to_first_frame of this VideoView.  # noqa: E501


        :return: The time_to_first_frame of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._time_to_first_frame

    @time_to_first_frame.setter
    def time_to_first_frame(self, time_to_first_frame):
        """Sets the time_to_first_frame of this VideoView.


        :param time_to_first_frame: The time_to_first_frame of this VideoView.  # noqa: E501
        :type: int
        """

        self._time_to_first_frame = time_to_first_frame

    @property
    def viewer_user_id(self):
        """Gets the viewer_user_id of this VideoView.  # noqa: E501


        :return: The viewer_user_id of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_user_id

    @viewer_user_id.setter
    def viewer_user_id(self, viewer_user_id):
        """Sets the viewer_user_id of this VideoView.


        :param viewer_user_id: The viewer_user_id of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_user_id = viewer_user_id

    @property
    def video_stream_type(self):
        """Gets the video_stream_type of this VideoView.  # noqa: E501


        :return: The video_stream_type of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_stream_type

    @video_stream_type.setter
    def video_stream_type(self, video_stream_type):
        """Sets the video_stream_type of this VideoView.


        :param video_stream_type: The video_stream_type of this VideoView.  # noqa: E501
        :type: str
        """

        self._video_stream_type = video_stream_type

    @property
    def player_startup_time(self):
        """Gets the player_startup_time of this VideoView.  # noqa: E501


        :return: The player_startup_time of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_startup_time

    @player_startup_time.setter
    def player_startup_time(self, player_startup_time):
        """Sets the player_startup_time of this VideoView.


        :param player_startup_time: The player_startup_time of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_startup_time = player_startup_time

    @property
    def viewer_application_version(self):
        """Gets the viewer_application_version of this VideoView.  # noqa: E501


        :return: The viewer_application_version of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_application_version

    @viewer_application_version.setter
    def viewer_application_version(self, viewer_application_version):
        """Sets the viewer_application_version of this VideoView.


        :param viewer_application_version: The viewer_application_version of this VideoView.  # noqa: E501
        :type: str
        """

        self._viewer_application_version = viewer_application_version

    @property
    def view_max_downscale_percentage(self):
        """Gets the view_max_downscale_percentage of this VideoView.  # noqa: E501


        :return: The view_max_downscale_percentage of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_max_downscale_percentage

    @view_max_downscale_percentage.setter
    def view_max_downscale_percentage(self, view_max_downscale_percentage):
        """Sets the view_max_downscale_percentage of this VideoView.


        :param view_max_downscale_percentage: The view_max_downscale_percentage of this VideoView.  # noqa: E501
        :type: str
        """

        self._view_max_downscale_percentage = view_max_downscale_percentage

    @property
    def view_max_upscale_percentage(self):
        """Gets the view_max_upscale_percentage of this VideoView.  # noqa: E501


        :return: The view_max_upscale_percentage of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_max_upscale_percentage

    @view_max_upscale_percentage.setter
    def view_max_upscale_percentage(self, view_max_upscale_percentage):
        """Sets the view_max_upscale_percentage of this VideoView.


        :param view_max_upscale_percentage: The view_max_upscale_percentage of this VideoView.  # noqa: E501
        :type: str
        """

        self._view_max_upscale_percentage = view_max_upscale_percentage

    @property
    def country_code(self):
        """Gets the country_code of this VideoView.  # noqa: E501


        :return: The country_code of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this VideoView.


        :param country_code: The country_code of this VideoView.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def used_fullscreen(self):
        """Gets the used_fullscreen of this VideoView.  # noqa: E501


        :return: The used_fullscreen of this VideoView.  # noqa: E501
        :rtype: bool
        """
        return self._used_fullscreen

    @used_fullscreen.setter
    def used_fullscreen(self, used_fullscreen):
        """Sets the used_fullscreen of this VideoView.


        :param used_fullscreen: The used_fullscreen of this VideoView.  # noqa: E501
        :type: bool
        """

        self._used_fullscreen = used_fullscreen

    @property
    def isp(self):
        """Gets the isp of this VideoView.  # noqa: E501


        :return: The isp of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this VideoView.


        :param isp: The isp of this VideoView.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def property_id(self):
        """Gets the property_id of this VideoView.  # noqa: E501


        :return: The property_id of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this VideoView.


        :param property_id: The property_id of this VideoView.  # noqa: E501
        :type: int
        """

        self._property_id = property_id

    @property
    def player_autoplay(self):
        """Gets the player_autoplay of this VideoView.  # noqa: E501


        :return: The player_autoplay of this VideoView.  # noqa: E501
        :rtype: bool
        """
        return self._player_autoplay

    @player_autoplay.setter
    def player_autoplay(self, player_autoplay):
        """Sets the player_autoplay of this VideoView.


        :param player_autoplay: The player_autoplay of this VideoView.  # noqa: E501
        :type: bool
        """

        self._player_autoplay = player_autoplay

    @property
    def player_height(self):
        """Gets the player_height of this VideoView.  # noqa: E501


        :return: The player_height of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._player_height

    @player_height.setter
    def player_height(self, player_height):
        """Sets the player_height of this VideoView.


        :param player_height: The player_height of this VideoView.  # noqa: E501
        :type: int
        """

        self._player_height = player_height

    @property
    def asn(self):
        """Gets the asn of this VideoView.  # noqa: E501


        :return: The asn of this VideoView.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this VideoView.


        :param asn: The asn of this VideoView.  # noqa: E501
        :type: int
        """

        self._asn = asn

    @property
    def asn_name(self):
        """Gets the asn_name of this VideoView.  # noqa: E501


        :return: The asn_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._asn_name

    @asn_name.setter
    def asn_name(self, asn_name):
        """Sets the asn_name of this VideoView.


        :param asn_name: The asn_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._asn_name = asn_name

    @property
    def quality_score(self):
        """Gets the quality_score of this VideoView.  # noqa: E501


        :return: The quality_score of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._quality_score

    @quality_score.setter
    def quality_score(self, quality_score):
        """Sets the quality_score of this VideoView.


        :param quality_score: The quality_score of this VideoView.  # noqa: E501
        :type: str
        """

        self._quality_score = quality_score

    @property
    def player_software_version(self):
        """Gets the player_software_version of this VideoView.  # noqa: E501


        :return: The player_software_version of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_software_version

    @player_software_version.setter
    def player_software_version(self, player_software_version):
        """Sets the player_software_version of this VideoView.


        :param player_software_version: The player_software_version of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_software_version = player_software_version

    @property
    def player_mux_plugin_name(self):
        """Gets the player_mux_plugin_name of this VideoView.  # noqa: E501


        :return: The player_mux_plugin_name of this VideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_mux_plugin_name

    @player_mux_plugin_name.setter
    def player_mux_plugin_name(self, player_mux_plugin_name):
        """Sets the player_mux_plugin_name of this VideoView.


        :param player_mux_plugin_name: The player_mux_plugin_name of this VideoView.  # noqa: E501
        :type: str
        """

        self._player_mux_plugin_name = player_mux_plugin_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VideoView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
