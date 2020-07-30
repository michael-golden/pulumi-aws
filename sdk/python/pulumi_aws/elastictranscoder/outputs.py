# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'PipelineContentConfig',
    'PipelineContentConfigPermission',
    'PipelineNotifications',
    'PipelineThumbnailConfig',
    'PipelineThumbnailConfigPermission',
    'PresetAudio',
    'PresetAudioCodecOptions',
    'PresetThumbnails',
    'PresetVideo',
    'PresetVideoWatermark',
]

@pulumi.output_type
class PipelineContentConfig(dict):
    bucket: Optional[str] = pulumi.output_property("bucket")
    """
    The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
    """
    storage_class: Optional[str] = pulumi.output_property("storageClass")
    """
    The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PipelineContentConfigPermission(dict):
    accesses: Optional[List[str]] = pulumi.output_property("accesses")
    """
    The permission that you want to give to the AWS user that you specified in `content_config_permissions.grantee`
    """
    grantee: Optional[str] = pulumi.output_property("grantee")
    """
    The AWS user or group that you want to have access to transcoded files and playlists.
    """
    grantee_type: Optional[str] = pulumi.output_property("granteeType")
    """
    Specify the type of value that appears in the `content_config_permissions.grantee` object. Valid values are `Canonical`, `Email` or `Group`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PipelineNotifications(dict):
    completed: Optional[str] = pulumi.output_property("completed")
    """
    The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
    """
    error: Optional[str] = pulumi.output_property("error")
    """
    The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
    """
    progressing: Optional[str] = pulumi.output_property("progressing")
    """
    The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
    """
    warning: Optional[str] = pulumi.output_property("warning")
    """
    The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PipelineThumbnailConfig(dict):
    bucket: Optional[str] = pulumi.output_property("bucket")
    """
    The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
    """
    storage_class: Optional[str] = pulumi.output_property("storageClass")
    """
    The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PipelineThumbnailConfigPermission(dict):
    accesses: Optional[List[str]] = pulumi.output_property("accesses")
    """
    The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
    """
    grantee: Optional[str] = pulumi.output_property("grantee")
    """
    The AWS user or group that you want to have access to thumbnail files.
    """
    grantee_type: Optional[str] = pulumi.output_property("granteeType")
    """
    Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PresetAudio(dict):
    audio_packing_mode: Optional[str] = pulumi.output_property("audioPackingMode")
    """
    The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
    """
    bit_rate: Optional[str] = pulumi.output_property("bitRate")
    """
    The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.
    """
    channels: Optional[str] = pulumi.output_property("channels")
    """
    The number of audio channels in the output file
    """
    codec: Optional[str] = pulumi.output_property("codec")
    """
    The audio codec for the output file. Valid values are `AAC`, `flac`, `mp2`, `mp3`, `pcm`, and `vorbis`.
    """
    sample_rate: Optional[str] = pulumi.output_property("sampleRate")
    """
    The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PresetAudioCodecOptions(dict):
    bit_depth: Optional[str] = pulumi.output_property("bitDepth")
    """
    The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
    """
    bit_order: Optional[str] = pulumi.output_property("bitOrder")
    """
    The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
    """
    profile: Optional[str] = pulumi.output_property("profile")
    """
    If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
    """
    signed: Optional[str] = pulumi.output_property("signed")
    """
    Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PresetThumbnails(dict):
    aspect_ratio: Optional[str] = pulumi.output_property("aspectRatio")
    """
    The aspect ratio of thumbnails. The following values are valid: auto, 1:1, 4:3, 3:2, 16:9
    """
    format: Optional[str] = pulumi.output_property("format")
    """
    The format of thumbnails, if any. Valid formats are jpg and png.
    """
    interval: Optional[str] = pulumi.output_property("interval")
    """
    The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
    """
    max_height: Optional[str] = pulumi.output_property("maxHeight")
    """
    The maximum height of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.
    """
    max_width: Optional[str] = pulumi.output_property("maxWidth")
    """
    The maximum width of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.
    """
    padding_policy: Optional[str] = pulumi.output_property("paddingPolicy")
    """
    When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail MaxWidth and MaxHeight settings.
    """
    resolution: Optional[str] = pulumi.output_property("resolution")
    """
    The width and height of thumbnail files in pixels, in the format WidthxHeight, where both values are even integers. The values cannot exceed the width and height that you specified in the Video:Resolution object. (To better control resolution and aspect ratio of thumbnails, we recommend that you use the thumbnail values `max_width`, `max_height`, `sizing_policy`, and `padding_policy` instead of `resolution` and `aspect_ratio`. The two groups of settings are mutually exclusive. Do not use them together)
    """
    sizing_policy: Optional[str] = pulumi.output_property("sizingPolicy")
    """
    A value that controls scaling of thumbnails. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, and `ShrinkToFill`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PresetVideo(dict):
    aspect_ratio: Optional[str] = pulumi.output_property("aspectRatio")
    """
    The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
    """
    bit_rate: Optional[str] = pulumi.output_property("bitRate")
    """
    The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
    """
    codec: Optional[str] = pulumi.output_property("codec")
    """
    The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
    """
    display_aspect_ratio: Optional[str] = pulumi.output_property("displayAspectRatio")
    """
    The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
    """
    fixed_gop: Optional[str] = pulumi.output_property("fixedGop")
    """
    Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
    """
    frame_rate: Optional[str] = pulumi.output_property("frameRate")
    """
    The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
    """
    keyframes_max_dist: Optional[str] = pulumi.output_property("keyframesMaxDist")
    """
    The maximum number of frames between key frames. Not applicable for containers of type gif.
    """
    max_frame_rate: Optional[str] = pulumi.output_property("maxFrameRate")
    """
    If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
    """
    max_height: Optional[str] = pulumi.output_property("maxHeight")
    """
    The maximum height of the output video in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 96 and 3072, inclusive.
    """
    max_width: Optional[str] = pulumi.output_property("maxWidth")
    """
    The maximum width of the output video in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 128 and 4096, inclusive.
    """
    padding_policy: Optional[str] = pulumi.output_property("paddingPolicy")
    """
    When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
    """
    resolution: Optional[str] = pulumi.output_property("resolution")
    """
    The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
    """
    sizing_policy: Optional[str] = pulumi.output_property("sizingPolicy")
    """
    A value that controls scaling of the output video. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, `ShrinkToFill`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PresetVideoWatermark(dict):
    horizontal_align: Optional[str] = pulumi.output_property("horizontalAlign")
    """
    The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
    """
    horizontal_offset: Optional[str] = pulumi.output_property("horizontalOffset")
    """
    The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
    """
    id: Optional[str] = pulumi.output_property("id")
    """
    A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
    """
    max_height: Optional[str] = pulumi.output_property("maxHeight")
    """
    The maximum height of the watermark.
    """
    max_width: Optional[str] = pulumi.output_property("maxWidth")
    """
    The maximum width of the watermark.
    """
    opacity: Optional[str] = pulumi.output_property("opacity")
    """
    A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
    """
    sizing_policy: Optional[str] = pulumi.output_property("sizingPolicy")
    """
    A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
    """
    target: Optional[str] = pulumi.output_property("target")
    """
    A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
    """
    vertical_align: Optional[str] = pulumi.output_property("verticalAlign")
    """
    The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
    """
    vertical_offset: Optional[str] = pulumi.output_property("verticalOffset")
    """
    The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


