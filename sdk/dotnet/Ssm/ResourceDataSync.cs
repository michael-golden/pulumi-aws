// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ssm
{
    /// <summary>
    /// Provides a SSM resource data sync.
    /// 
    /// 
    /// ## s3_destination
    /// 
    /// `s3_destination` supports the following:
    /// 
    /// * `bucket_name` - (Required) Name of S3 bucket where the aggregated data is stored.
    /// * `region` - (Required) Region with the bucket targeted by the Resource Data Sync.
    /// * `kms_key_arn` - (Optional) ARN of an encryption key for a destination in Amazon S3.
    /// * `prefix` - (Optional) Prefix for the bucket.
    /// * `sync_format` - (Optional) A supported sync format. Only JsonSerDe is currently supported. Defaults to JsonSerDe.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_resource_data_sync.html.markdown.
    /// </summary>
    public partial class ResourceDataSync : Pulumi.CustomResource
    {
        /// <summary>
        /// Name for the configuration.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Amazon S3 configuration details for the sync.
        /// </summary>
        [Output("s3Destination")]
        public Output<Outputs.ResourceDataSyncS3Destination> S3Destination { get; private set; } = null!;


        /// <summary>
        /// Create a ResourceDataSync resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResourceDataSync(string name, ResourceDataSyncArgs args, CustomResourceOptions? options = null)
            : base("aws:ssm/resourceDataSync:ResourceDataSync", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ResourceDataSync(string name, Input<string> id, ResourceDataSyncState? state = null, CustomResourceOptions? options = null)
            : base("aws:ssm/resourceDataSync:ResourceDataSync", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ResourceDataSync resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResourceDataSync Get(string name, Input<string> id, ResourceDataSyncState? state = null, CustomResourceOptions? options = null)
        {
            return new ResourceDataSync(name, id, state, options);
        }
    }

    public sealed class ResourceDataSyncArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name for the configuration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Amazon S3 configuration details for the sync.
        /// </summary>
        [Input("s3Destination", required: true)]
        public Input<Inputs.ResourceDataSyncS3DestinationArgs> S3Destination { get; set; } = null!;

        public ResourceDataSyncArgs()
        {
        }
    }

    public sealed class ResourceDataSyncState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name for the configuration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Amazon S3 configuration details for the sync.
        /// </summary>
        [Input("s3Destination")]
        public Input<Inputs.ResourceDataSyncS3DestinationGetArgs>? S3Destination { get; set; }

        public ResourceDataSyncState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ResourceDataSyncS3DestinationArgs : Pulumi.ResourceArgs
    {
        [Input("bucketName", required: true)]
        public Input<string> BucketName { get; set; } = null!;

        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        [Input("syncFormat")]
        public Input<string>? SyncFormat { get; set; }

        public ResourceDataSyncS3DestinationArgs()
        {
        }
    }

    public sealed class ResourceDataSyncS3DestinationGetArgs : Pulumi.ResourceArgs
    {
        [Input("bucketName", required: true)]
        public Input<string> BucketName { get; set; } = null!;

        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        [Input("syncFormat")]
        public Input<string>? SyncFormat { get; set; }

        public ResourceDataSyncS3DestinationGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ResourceDataSyncS3Destination
    {
        public readonly string BucketName;
        public readonly string? KmsKeyArn;
        public readonly string? Prefix;
        public readonly string Region;
        public readonly string? SyncFormat;

        [OutputConstructor]
        private ResourceDataSyncS3Destination(
            string bucketName,
            string? kmsKeyArn,
            string? prefix,
            string region,
            string? syncFormat)
        {
            BucketName = bucketName;
            KmsKeyArn = kmsKeyArn;
            Prefix = prefix;
            Region = region;
            SyncFormat = syncFormat;
        }
    }
    }
}
