// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Kinesis
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get information about a Kinesis Stream for use in other
        /// resources.
        /// 
        /// For more details, see the [Amazon Kinesis Documentation][1].
        /// 
        /// 
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kinesis_stream.html.markdown.
        /// </summary>
        [Obsolete("Use GetStream.InvokeAsync() instead")]
        public static Task<GetStreamResult> GetStream(GetStreamArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetStreamResult>("aws:kinesis/getStream:getStream", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetStream
    {
        /// <summary>
        /// Use this data source to get information about a Kinesis Stream for use in other
        /// resources.
        /// 
        /// For more details, see the [Amazon Kinesis Documentation][1].
        /// 
        /// 
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kinesis_stream.html.markdown.
        /// </summary>
        public static Task<GetStreamResult> InvokeAsync(GetStreamArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetStreamResult>("aws:kinesis/getStream:getStream", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetStreamArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Kinesis Stream.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        [Input("tags")]
        private Dictionary<string, object>? _tags;

        /// <summary>
        /// A mapping of tags to assigned to the stream.
        /// </summary>
        public Dictionary<string, object> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, object>());
            set => _tags = value;
        }

        public GetStreamArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetStreamResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).
        /// </summary>
        public readonly string Arn;
        /// <summary>
        /// The list of shard ids in the CLOSED state. See [Shard State][2] for more.
        /// </summary>
        public readonly ImmutableArray<string> ClosedShards;
        /// <summary>
        /// The approximate UNIX timestamp that the stream was created.
        /// </summary>
        public readonly int CreationTimestamp;
        /// <summary>
        /// The name of the Kinesis Stream.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The list of shard ids in the OPEN state. See [Shard State][2] for more.
        /// </summary>
        public readonly ImmutableArray<string> OpenShards;
        /// <summary>
        /// Length of time (in hours) data records are accessible after they are added to the stream.
        /// </summary>
        public readonly int RetentionPeriod;
        /// <summary>
        /// A list of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with CloudWatch][3] for more.
        /// </summary>
        public readonly ImmutableArray<string> ShardLevelMetrics;
        /// <summary>
        /// The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// A mapping of tags to assigned to the stream.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Tags;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetStreamResult(
            string arn,
            ImmutableArray<string> closedShards,
            int creationTimestamp,
            string name,
            ImmutableArray<string> openShards,
            int retentionPeriod,
            ImmutableArray<string> shardLevelMetrics,
            string status,
            ImmutableDictionary<string, object> tags,
            string id)
        {
            Arn = arn;
            ClosedShards = closedShards;
            CreationTimestamp = creationTimestamp;
            Name = name;
            OpenShards = openShards;
            RetentionPeriod = retentionPeriod;
            ShardLevelMetrics = shardLevelMetrics;
            Status = status;
            Tags = tags;
            Id = id;
        }
    }
}
