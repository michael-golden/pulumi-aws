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
    /// Manages S3 bucket-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleBucket = new Aws.S3.Bucket("exampleBucket", new Aws.S3.BucketArgs
    ///         {
    ///         });
    ///         var exampleBucketPublicAccessBlock = new Aws.S3.BucketPublicAccessBlock("exampleBucketPublicAccessBlock", new Aws.S3.BucketPublicAccessBlockArgs
    ///         {
    ///             Bucket = exampleBucket.Id,
    ///             BlockPublicAcls = true,
    ///             BlockPublicPolicy = true,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class BucketPublicAccessBlock : Pulumi.CustomResource
    {
        /// <summary>
        /// Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
        /// * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
        /// * PUT Object calls will fail if the request includes an object ACL.
        /// </summary>
        [Output("blockPublicAcls")]
        public Output<bool?> BlockPublicAcls { get; private set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
        /// * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        /// </summary>
        [Output("blockPublicPolicy")]
        public Output<bool?> BlockPublicPolicy { get; private set; } = null!;

        /// <summary>
        /// S3 Bucket to which this Public Access Block configuration should be applied.
        /// </summary>
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
        /// * Ignore public ACLs on this bucket and any objects that it contains.
        /// </summary>
        [Output("ignorePublicAcls")]
        public Output<bool?> IgnorePublicAcls { get; private set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
        /// * Only the bucket owner and AWS Services can access this buckets if it has a public policy.
        /// </summary>
        [Output("restrictPublicBuckets")]
        public Output<bool?> RestrictPublicBuckets { get; private set; } = null!;


        /// <summary>
        /// Create a BucketPublicAccessBlock resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BucketPublicAccessBlock(string name, BucketPublicAccessBlockArgs args, CustomResourceOptions? options = null)
            : base("aws:s3/bucketPublicAccessBlock:BucketPublicAccessBlock", name, args ?? new BucketPublicAccessBlockArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BucketPublicAccessBlock(string name, Input<string> id, BucketPublicAccessBlockState? state = null, CustomResourceOptions? options = null)
            : base("aws:s3/bucketPublicAccessBlock:BucketPublicAccessBlock", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing BucketPublicAccessBlock resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BucketPublicAccessBlock Get(string name, Input<string> id, BucketPublicAccessBlockState? state = null, CustomResourceOptions? options = null)
        {
            return new BucketPublicAccessBlock(name, id, state, options);
        }
    }

    public sealed class BucketPublicAccessBlockArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
        /// * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
        /// * PUT Object calls will fail if the request includes an object ACL.
        /// </summary>
        [Input("blockPublicAcls")]
        public Input<bool>? BlockPublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
        /// * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        /// </summary>
        [Input("blockPublicPolicy")]
        public Input<bool>? BlockPublicPolicy { get; set; }

        /// <summary>
        /// S3 Bucket to which this Public Access Block configuration should be applied.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
        /// * Ignore public ACLs on this bucket and any objects that it contains.
        /// </summary>
        [Input("ignorePublicAcls")]
        public Input<bool>? IgnorePublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
        /// * Only the bucket owner and AWS Services can access this buckets if it has a public policy.
        /// </summary>
        [Input("restrictPublicBuckets")]
        public Input<bool>? RestrictPublicBuckets { get; set; }

        public BucketPublicAccessBlockArgs()
        {
        }
    }

    public sealed class BucketPublicAccessBlockState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
        /// * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
        /// * PUT Object calls will fail if the request includes an object ACL.
        /// </summary>
        [Input("blockPublicAcls")]
        public Input<bool>? BlockPublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
        /// * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        /// </summary>
        [Input("blockPublicPolicy")]
        public Input<bool>? BlockPublicPolicy { get; set; }

        /// <summary>
        /// S3 Bucket to which this Public Access Block configuration should be applied.
        /// </summary>
        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        /// <summary>
        /// Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
        /// * Ignore public ACLs on this bucket and any objects that it contains.
        /// </summary>
        [Input("ignorePublicAcls")]
        public Input<bool>? IgnorePublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
        /// * Only the bucket owner and AWS Services can access this buckets if it has a public policy.
        /// </summary>
        [Input("restrictPublicBuckets")]
        public Input<bool>? RestrictPublicBuckets { get; set; }

        public BucketPublicAccessBlockState()
        {
        }
    }
}
