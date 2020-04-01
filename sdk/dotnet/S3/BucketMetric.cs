// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.S3
{
    /// <summary>
    /// Provides a S3 bucket [metrics configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html) resource.
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_metric.html.markdown.
    /// </summary>
    public partial class BucketMetric : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the bucket to put metric configuration.
        /// </summary>
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        /// <summary>
        /// [Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        /// </summary>
        [Output("filter")]
        public Output<Outputs.BucketMetricFilter?> Filter { get; private set; } = null!;

        /// <summary>
        /// Unique identifier of the metrics configuration for the bucket.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a BucketMetric resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BucketMetric(string name, BucketMetricArgs args, CustomResourceOptions? options = null)
            : base("aws:s3/bucketMetric:BucketMetric", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private BucketMetric(string name, Input<string> id, BucketMetricState? state = null, CustomResourceOptions? options = null)
            : base("aws:s3/bucketMetric:BucketMetric", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BucketMetric resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BucketMetric Get(string name, Input<string> id, BucketMetricState? state = null, CustomResourceOptions? options = null)
        {
            return new BucketMetric(name, id, state, options);
        }
    }

    public sealed class BucketMetricArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the bucket to put metric configuration.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// [Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        /// </summary>
        [Input("filter")]
        public Input<Inputs.BucketMetricFilterArgs>? Filter { get; set; }

        /// <summary>
        /// Unique identifier of the metrics configuration for the bucket.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public BucketMetricArgs()
        {
        }
    }

    public sealed class BucketMetricState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the bucket to put metric configuration.
        /// </summary>
        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        /// <summary>
        /// [Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        /// </summary>
        [Input("filter")]
        public Input<Inputs.BucketMetricFilterGetArgs>? Filter { get; set; }

        /// <summary>
        /// Unique identifier of the metrics configuration for the bucket.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public BucketMetricState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class BucketMetricFilterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Object prefix for filtering (singular).
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Object tags for filtering (up to 10).
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public BucketMetricFilterArgs()
        {
        }
    }

    public sealed class BucketMetricFilterGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Object prefix for filtering (singular).
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Object tags for filtering (up to 10).
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public BucketMetricFilterGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class BucketMetricFilter
    {
        /// <summary>
        /// Object prefix for filtering (singular).
        /// </summary>
        public readonly string? Prefix;
        /// <summary>
        /// Object tags for filtering (up to 10).
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Tags;

        [OutputConstructor]
        private BucketMetricFilter(
            string? prefix,
            ImmutableDictionary<string, object>? tags)
        {
            Prefix = prefix;
            Tags = tags;
        }
    }
    }
}
