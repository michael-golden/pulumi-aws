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
    /// Manages S3 account-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).
    /// 
    /// &gt; **NOTE:** Each AWS account may only have one S3 Public Access Block configuration. Multiple configurations of the resource against the same AWS account will cause a perpetual difference.
    /// 
    /// &gt; Advanced usage: To use a custom API endpoint for this resource, use the [`s3control` endpoint provider configuration](https://www.terraform.io/docs/providers/aws/index.html#s3control), not the `s3` endpoint provider configuration.
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_account_public_access_block.html.markdown.
    /// </summary>
    public partial class AccountPublicAccessBlock : Pulumi.CustomResource
    {
        /// <summary>
        /// AWS account ID to configure. Defaults to automatically determined account ID of the this provider AWS provider.
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
        /// * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
        /// * PUT Object calls will fail if the request includes an object ACL.
        /// </summary>
        [Output("blockPublicAcls")]
        public Output<bool?> BlockPublicAcls { get; private set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
        /// * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        /// </summary>
        [Output("blockPublicPolicy")]
        public Output<bool?> BlockPublicPolicy { get; private set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
        /// * Ignore all public ACLs on buckets in this account and any objects that they contain.
        /// </summary>
        [Output("ignorePublicAcls")]
        public Output<bool?> IgnorePublicAcls { get; private set; } = null!;

        /// <summary>
        /// Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
        /// * Only the bucket owner and AWS Services can access buckets with public policies.
        /// </summary>
        [Output("restrictPublicBuckets")]
        public Output<bool?> RestrictPublicBuckets { get; private set; } = null!;


        /// <summary>
        /// Create a AccountPublicAccessBlock resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AccountPublicAccessBlock(string name, AccountPublicAccessBlockArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:s3/accountPublicAccessBlock:AccountPublicAccessBlock", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private AccountPublicAccessBlock(string name, Input<string> id, AccountPublicAccessBlockState? state = null, CustomResourceOptions? options = null)
            : base("aws:s3/accountPublicAccessBlock:AccountPublicAccessBlock", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AccountPublicAccessBlock resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AccountPublicAccessBlock Get(string name, Input<string> id, AccountPublicAccessBlockState? state = null, CustomResourceOptions? options = null)
        {
            return new AccountPublicAccessBlock(name, id, state, options);
        }
    }

    public sealed class AccountPublicAccessBlockArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// AWS account ID to configure. Defaults to automatically determined account ID of the this provider AWS provider.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
        /// * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
        /// * PUT Object calls will fail if the request includes an object ACL.
        /// </summary>
        [Input("blockPublicAcls")]
        public Input<bool>? BlockPublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
        /// * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        /// </summary>
        [Input("blockPublicPolicy")]
        public Input<bool>? BlockPublicPolicy { get; set; }

        /// <summary>
        /// Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
        /// * Ignore all public ACLs on buckets in this account and any objects that they contain.
        /// </summary>
        [Input("ignorePublicAcls")]
        public Input<bool>? IgnorePublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
        /// * Only the bucket owner and AWS Services can access buckets with public policies.
        /// </summary>
        [Input("restrictPublicBuckets")]
        public Input<bool>? RestrictPublicBuckets { get; set; }

        public AccountPublicAccessBlockArgs()
        {
        }
    }

    public sealed class AccountPublicAccessBlockState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// AWS account ID to configure. Defaults to automatically determined account ID of the this provider AWS provider.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
        /// * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
        /// * PUT Object calls will fail if the request includes an object ACL.
        /// </summary>
        [Input("blockPublicAcls")]
        public Input<bool>? BlockPublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
        /// * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        /// </summary>
        [Input("blockPublicPolicy")]
        public Input<bool>? BlockPublicPolicy { get; set; }

        /// <summary>
        /// Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
        /// * Ignore all public ACLs on buckets in this account and any objects that they contain.
        /// </summary>
        [Input("ignorePublicAcls")]
        public Input<bool>? IgnorePublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
        /// * Only the bucket owner and AWS Services can access buckets with public policies.
        /// </summary>
        [Input("restrictPublicBuckets")]
        public Input<bool>? RestrictPublicBuckets { get; set; }

        public AccountPublicAccessBlockState()
        {
        }
    }
}
