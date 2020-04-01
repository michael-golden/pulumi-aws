// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Macie
{
    /// <summary>
    /// Associates an S3 resource with Amazon Macie for monitoring and data classification.
    /// 
    /// &gt; **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/macie_s3_bucket_association.html.markdown.
    /// </summary>
    public partial class S3BucketAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the S3 bucket that you want to associate with Amazon Macie.
        /// </summary>
        [Output("bucketName")]
        public Output<string> BucketName { get; private set; } = null!;

        /// <summary>
        /// The configuration of how Amazon Macie classifies the S3 objects.
        /// </summary>
        [Output("classificationType")]
        public Output<Outputs.S3BucketAssociationClassificationType> ClassificationType { get; private set; } = null!;

        /// <summary>
        /// The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.
        /// </summary>
        [Output("memberAccountId")]
        public Output<string?> MemberAccountId { get; private set; } = null!;

        /// <summary>
        /// Object key prefix identifying one or more S3 objects to which the association applies.
        /// </summary>
        [Output("prefix")]
        public Output<string?> Prefix { get; private set; } = null!;


        /// <summary>
        /// Create a S3BucketAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public S3BucketAssociation(string name, S3BucketAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws:macie/s3BucketAssociation:S3BucketAssociation", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private S3BucketAssociation(string name, Input<string> id, S3BucketAssociationState? state = null, CustomResourceOptions? options = null)
            : base("aws:macie/s3BucketAssociation:S3BucketAssociation", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing S3BucketAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static S3BucketAssociation Get(string name, Input<string> id, S3BucketAssociationState? state = null, CustomResourceOptions? options = null)
        {
            return new S3BucketAssociation(name, id, state, options);
        }
    }

    public sealed class S3BucketAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the S3 bucket that you want to associate with Amazon Macie.
        /// </summary>
        [Input("bucketName", required: true)]
        public Input<string> BucketName { get; set; } = null!;

        /// <summary>
        /// The configuration of how Amazon Macie classifies the S3 objects.
        /// </summary>
        [Input("classificationType")]
        public Input<Inputs.S3BucketAssociationClassificationTypeArgs>? ClassificationType { get; set; }

        /// <summary>
        /// The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.
        /// </summary>
        [Input("memberAccountId")]
        public Input<string>? MemberAccountId { get; set; }

        /// <summary>
        /// Object key prefix identifying one or more S3 objects to which the association applies.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        public S3BucketAssociationArgs()
        {
        }
    }

    public sealed class S3BucketAssociationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the S3 bucket that you want to associate with Amazon Macie.
        /// </summary>
        [Input("bucketName")]
        public Input<string>? BucketName { get; set; }

        /// <summary>
        /// The configuration of how Amazon Macie classifies the S3 objects.
        /// </summary>
        [Input("classificationType")]
        public Input<Inputs.S3BucketAssociationClassificationTypeGetArgs>? ClassificationType { get; set; }

        /// <summary>
        /// The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.
        /// </summary>
        [Input("memberAccountId")]
        public Input<string>? MemberAccountId { get; set; }

        /// <summary>
        /// Object key prefix identifying one or more S3 objects to which the association applies.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        public S3BucketAssociationState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class S3BucketAssociationClassificationTypeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
        /// The only valid value is the default value, `FULL`.
        /// </summary>
        [Input("continuous")]
        public Input<string>? Continuous { get; set; }

        /// <summary>
        /// A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
        /// Valid values are `NONE` and `FULL`. Defaults to `NONE` indicating that Macie only classifies objects that are added after the association was created.
        /// </summary>
        [Input("oneTime")]
        public Input<string>? OneTime { get; set; }

        public S3BucketAssociationClassificationTypeArgs()
        {
        }
    }

    public sealed class S3BucketAssociationClassificationTypeGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
        /// The only valid value is the default value, `FULL`.
        /// </summary>
        [Input("continuous")]
        public Input<string>? Continuous { get; set; }

        /// <summary>
        /// A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
        /// Valid values are `NONE` and `FULL`. Defaults to `NONE` indicating that Macie only classifies objects that are added after the association was created.
        /// </summary>
        [Input("oneTime")]
        public Input<string>? OneTime { get; set; }

        public S3BucketAssociationClassificationTypeGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class S3BucketAssociationClassificationType
    {
        /// <summary>
        /// A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
        /// The only valid value is the default value, `FULL`.
        /// </summary>
        public readonly string? Continuous;
        /// <summary>
        /// A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
        /// Valid values are `NONE` and `FULL`. Defaults to `NONE` indicating that Macie only classifies objects that are added after the association was created.
        /// </summary>
        public readonly string? OneTime;

        [OutputConstructor]
        private S3BucketAssociationClassificationType(
            string? continuous,
            string? oneTime)
        {
            Continuous = continuous;
            OneTime = oneTime;
        }
    }
    }
}
